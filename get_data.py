import csv
import numpy as np
import random


def get_data():

  with open('train_2008.csv', 'r') as dest_f:

    data_iter = csv.reader(dest_f, delimiter = ",", quotechar = '"')
    data = [data for data in data_iter]

      # print data[0]
  # print data[1]
  # print data[2]

  lables = data[0]
  data = data[1:]

  random.shuffle(data)

  X_train = np.array([map(int, datum[:-1]) for datum in data])
  y_train = np.array([int(datum[-1]) for datum in data])

  categorical_indices = []

  # for i in range(len(X_train[0])):
  #
  #     cnt = {}
  #     for X in X_train:
  #         if X[i] not in cnt:
  #             cnt[X[i]] = len(cnt)
  #
  #     print lables[i], cnt
  #
  #     if len(cnt) < 150:
  #         categorical_indices.append(i)
  #         for X in X_train:
  #             X[i] = cnt[X[i]]
  #
  #
  #
  #
  # enc = OneHotEncoder(categorical_features=categorical_indices)
  # enc.fit(X_train)



  # print X_train[0]
  # X_train = enc.transform(X_train).toarray()
  # for foo in X_train[0]:
  #     print ">", foo






  # Normalize data
  # row_means = X_train.mean(axis=1)
  # row_stds = X_train.std(axis=1)
  # X_train = X_train - row_means[:, np.newaxis]
  # X_train = X_train / row_stds[:, np.newaxis]


  # Split into a training set and a test set for validation
  X_test = X_train[:6400]
  y_test = y_train[:6400] - 1

  X_train = X_train[6400:]
  y_train = y_train[6400:] - 1


  return X_train, y_train, X_test, y_test


if __name__ == '__main__':
    X_train, y_train, X_test, y_test= get_data()

    y_train = list(y_train) + list(y_test)

    num_data = len(y_train)
    num_voters = len([y for y in y_train if y == 1])
    print num_data, num_voters, float(num_voters)/num_data
