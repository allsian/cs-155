import csv
import random
import numpy as np
from sklearn.preprocessing import OneHotEncoder

#DELETED_LABELS = ["HRHHID", "HRMONTH", "HRYEAR4", "HURESPLI", "HUFINAL", "HEPHONEO", "HUTYPEA", "HUTYPB", "HUTYPC", "HRINTSTA", "HRMIS", "HRHHID2", "HUBUSL1", "HUBUSL2", "HUBUSL3", "HUBUSL4", "PROLDRRP", "PEPARENT", "PESPOUSE", "PULINENO", "PUBUS1", "PUBUS2OT", "PUBUSCK1"]

USED_LABELS = ["HUFAMINC", "PEAGE", "PTDTRACE", "PESEX"]

NUMERICAL_LABELS = ["PEAGE", "PRINUSYR", "HUFAMINC"]

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

        # print len(X_train[0])

        deleted_indices = []

        for i, l in enumerate(labels):
            if l not in USED_LABELS:
                deleted_indices.append(i)

        # print deleted_indices

        X_train = np.delete(X_train, deleted_indices, 1)

        print len(X_train[0])

        numerical_indices = []

        for i, l in enumerate(labels):
            if l in NUMERICAL_LABELS:
                numerical_indices.append(i)


        categorical_indices = []

        for i in range(len(X_train[0])):

            if i in numerical_indices:
                continue

            cnt = {}
            for X in X_train:
                if X[i] not in cnt:
                    cnt[X[i]] = len(cnt)

            if len(cnt) < 150:
                categorical_indices.append(i)
                for X in X_train:
                    X[i] = cnt[X[i]]




        enc = OneHotEncoder(categorical_features=categorical_indices)
        enc.fit(X_train)


        X_train = enc.transform(X_train).toarray()

        print len(X_train[0])

        # Normalize data
        row_means = X_train.mean(axis=1)
        row_stds = X_train.std(axis=1)
        X_train = X_train - row_means[:, np.newaxis]
        X_train = X_train / row_stds[:, np.newaxis]


        # Split into a training set and a test set for validation
        X_test = X_train[:6400]
        y_test = y_train[:6400] - 1

        X_train = X_train[6400:]
        y_train = y_train[6400:] - 1

    return X_train, y_train, X_test, y_test
