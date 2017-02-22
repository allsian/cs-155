

import csv
import numpy as np
from sklearn import tree
from sklearn.preprocessing import OneHotEncoder
from collections import Counter

import format_data
import random

import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Flatten, Dropout



print "Getting Data"
X_train, y_train, X_val, y_val, X_test = format_data.get_formatted_data()
print "Got Data"







## Transforms output to one-hot encoding
y_train = keras.utils.np_utils.to_categorical(y_train, 2)
y_val = keras.utils.np_utils.to_categorical(y_val, 2)

print X_train.shape






## Create your own model here given the constraints in the problem
model = Sequential()
model.add(Dense(1000, input_shape=(len(X_train[0]),)))

model.add(Activation('sigmoid'))

model.add(Dense(400))
model.add(Activation('sigmoid'))

model.add(Dense(300))
model.add(Activation('sigmoid'))

model.add(Dense(200))
model.add(Activation('sigmoid'))

model.add(Dense(100))
model.add(Activation('sigmoid'))

## We use one-hot encoding, we now put 10 on our output layer
model.add(Dense(2))
model.add(Activation('softmax'))

## Printing a summary of the layers and weights in your model
model.summary()


## Since we are one-hot encoding the labels, we use 'categorical_crossentropy' as your loss.
model.compile(loss='categorical_crossentropy',optimizer='rmsprop', metrics=['accuracy'])

fit = model.fit(X_train, y_train, batch_size=128, nb_epoch=10,
    verbose=1)

## Printing the accuracy of our model, according to the loss function specified in model.compile above
score = model.evaluate(X_val, y_val, verbose=1)
print('Test score:', score[0])
print('Test accuracy:', score[1])







#
# for i in range(1, len(X_lables) - 1):
#
#     cnt = Counter()
#
#     for X in X_train:
#         cnt[X[i]] += 1
#
#     if len(cnt) > 20:
#         print X_lables[i], len(cnt)
