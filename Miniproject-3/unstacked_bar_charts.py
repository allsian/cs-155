

import numpy as np
import matplotlib.pyplot as plt


train_data = np.transpose(np.genfromtxt('project3data/data.txt', delimiter = '\t', dtype=None))

i_train_vector = train_data[0]
j_train_vector = train_data[1]
y_ij_train_vector = train_data[2]
