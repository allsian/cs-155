import numpy as np
import matplotlib.pyplot as plt
import prob2utils


data = np.genfromtxt('project3data/data.txt', delimiter = '\t', dtype=None)

movie_data = np.genfromtxt('project3data/movies.txt', delimiter = '\t', dtype=None)


transposed_data = np.transpose(data)

user_ids_vector = list(transposed_data[0])
movie_ids_vector = list(transposed_data[1])
rating_vector = list(transposed_data[2])

max_user_id = max(user_ids_vector)
max_movie_id = max(movie_ids_vector)

eta = 3e-2
reg = 1e-3

K = 20

U, V, err = prob2utils.train_model(max_user_id, max_movie_id, K, eta, reg, data)


a, s, b = np.linalg.svd(V)

# print a
# print s
# print b

a_tilde = a[:, :2]

V_tilde = np.dot(np.transpose(a_tilde), V)
#U_tilde = np.dot(np.transpose(a_tilde), U)




def make_plot(indices, title, file):

    points = np.asarray([V_tilde[:, i] for i in indices])
    labels = [movie_data[i-1][1] for i in indices]


    plt.subplots_adjust(bottom = 0.1)
    plt.scatter(points[:, 0], points[:, 1], marker='o')

    for label, x, y in zip(labels, points[:, 0], points[:, 1]):
        plt.annotate(
            label,
            xy=(x, y), xytext=(-20, 20),
            textcoords='offset points', ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
            arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))

    plt.title(title)
    plt.show()





if __name__ == '__main__':

    # nick_cage_x_tarantino_movie_indices = [1016, 276, 238, 298, 918, 56, 156, 346, 17, 92]
    # make_plot(nick_cage_x_tarantino_movie_indices)

    best_movie_indices = [134, 178, 50, 12, 603, 64, 318, 408, 169, 483]

    most_popular_indices = [121, 300, 294, 286, 1, 181, 258, 100, 50, 288]

    #other_movie_indices = [313, 144, 753, 780, 56, 71, 87, 183, 88, 699, 740, 739] + best_movie_indices

    accessible_inaccessable = [98, 94, 89, 71, 135, 520, 526, 88, 676, 751]

    crime = [12, 56, 100, 127, 156, 302, 902, 72, 273, 346]
    documentary = [32, 48, 884, 954, 973, 1547, 360, 1629, 1594, 1318]
    fantasy = [423, 755, 820, 892, 951, 1036, 1076, 1133, 1292, 1293]

    make_plot(accessible_inaccessable, "Random Movies", "random")
    make_plot(crime, "Crime Movies", "crime")
    make_plot(documentary, "Documentaries", "documentary")
    make_plot(fantasy, "Fantasy Movies", "fanstasy")
    make_plot(best_movie_indices, "Highest Rated Movies", "best")
    make_plot(most_popular_indices, "Most Rated Movies", "popular")
