import numpy as np
import matplotlib.pyplot as plt
import prob2utils


data = np.genfromtxt('project3data/data.txt', delimiter = '\t', dtype=None)

transposed_data = np.transpose(data)

user_ids_vector = list(data[0])
movie_ids_vector = list(data[1])
rating_vector = list(data[2])

eta = 3e-2
reg = 1e-2

K = 20

U, V, err = prob2utils.train_model(max(user_ids_vector), max(movie_ids_vector), K, eta, reg, data)
