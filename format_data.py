import csv
import random
import numpy as np
from sklearn.preprocessing import OneHotEncoder

#DELETED_LABELS = ["HRHHID", "HRMONTH", "HRYEAR4", "HURESPLI", "HUFINAL", "HEPHONEO", "HUTYPEA", "HUTYPB", "HUTYPC", "HRINTSTA", "HRMIS", "HRHHID2", "HUBUSL1", "HUBUSL2", "HUBUSL3", "HUBUSL4", "PROLDRRP", "PEPARENT", "PESPOUSE", "PULINENO", "PUBUS1", "PUBUS2OT", "PUBUSCK1"]

USED_LABELS = ["PEAGE", "PESEX"]

NUMERICAL_LABELS = ["PEAGE"]

CATEGORICAL_LABELS = ["PESEX"]


def transform_data(X_in, labels):
    deleted_indices = []

    for i, l in enumerate(labels):
        if l not in USED_LABELS:
            deleted_indices.append(i)

    # print deleted_indices

    X_in = np.delete(X_in, deleted_indices, 1)
    labels = [label for label in labels if label in USED_LABELS]

    print len(X_in[0])

    numerical_indices = []
    categorical_indices = []

    for i, l in enumerate(labels):
        if l in NUMERICAL_LABELS:
            numerical_indices.append(i)
        elif l in CATEGORICAL_LABELS:
            categorical_indices.append(i)


    for i in range(len(X_in[0])):
        if i in categorical_indices:
            remap_dict = {}
            for X in X_in:
                if X[i] not in remap_dict:
                    remap_dict[X[i]] = len(remap_dict)
            for X in X_in:
                X[i] = remap_dict[X[i]]
        '''
        elif i in categorical_indices:
            for X in X_in:
                if not X[i] > 0:
                    X[i] = 0
        '''



    if len(CATEGORICAL_LABELS) > 0:
        enc = OneHotEncoder(categorical_features=categorical_indices)
        enc.fit(X_in)
        X_in = enc.transform(X_in).toarray()

    print len(X_in[0])

    # Normalize data
    row_means = X_in.mean(axis=1)
    row_stds = X_in.std(axis=1)
    X_in = X_in - row_means[:, np.newaxis]
    X_in = X_in / row_stds[:, np.newaxis]
    return X_in

def get_test_data():
    with open('test_2008.csv', 'r') as dest_f:
        data_iter = csv.reader(dest_f, delimiter = ",", quotechar = '"')
        data = [data for data in data_iter]
        data = data[1:] # get rid of labels
        X_test = np.array([map(int, datum) for datum in data])
        return X_test

def get_formatted_data():
    with open('train_2008.csv', 'r') as dest_f:

        data_iter = csv.reader(dest_f, delimiter = ",", quotechar = '"')
        data = [data for data in data_iter]

        # print data[0]
        # print data[1]
        # print data[2]



        labels = data[0]
        data = data[1:]

        random.shuffle(data)


        X_train = np.array([map(int, datum[:-1]) for datum in data])
        y_train = np.array([int(datum[-1]) for datum in data])

        X_test = np.array(get_test_data())
        X_combined = np.concatenate((X_train, X_test), axis=0)

        X_combined = transform_data(X_combined, labels)
        X_train = X_combined[:len(X_train)]
        X_test = X_combined[len(X_train):]


        # Split into a training set and a test set for validation
        X_val = X_train[:6400]
        y_val = y_train[:6400] - 1

        X_train = X_train[6400:]
        y_train = y_train[6400:] - 1

    return X_train, y_train, X_val, y_val, X_test
