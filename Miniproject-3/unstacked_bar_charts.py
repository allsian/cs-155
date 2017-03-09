

import numpy as np
import matplotlib.pyplot as plt


data = np.transpose(np.genfromtxt('project3data/data.txt', delimiter = '\t', dtype=None))

user_ids_vector = list(data[0])
movie_ids_vector = list(data[1])
rating_vector = list(data[2])

genre_data = np.genfromtxt('project3data/movies.txt', delimiter = '\t', dtype=None)




rating_values = np.arange(1, 5+1)

relevant_ratings_list = [r for (m_id, r) in zip(movie_ids_vector, rating_vector)]

rating_counts = [relevant_ratings_list.count(r) for r in rating_values]


print rating_values
print rating_counts

width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(rating_values, rating_counts, width, color='r')

# add some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(rating_values + width / 2)
ax.set_xticklabels(('1', '2', '3', '4', '5'))


plt.title("Number of Ratings Across all Movies")
plt.xlabel("Rating")
plt.ylabel("Number of Ratings")


plt.savefig("visualizations/all_ratings_bar_chart.pdf")



for genre_index, genre_name in zip(range(3, 21), ["Action", "Adventure", "Animation", "Childrens", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"]):

    rating_values = np.arange(1, 5+1)

    relevant_ratings_list = [r for (m_id, r) in zip(movie_ids_vector, rating_vector) if genre_data[m_id-1][genre_index] == 1]

    rating_counts = [relevant_ratings_list.count(r) for r in rating_values]


    print rating_values
    print rating_counts

    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(rating_values, rating_counts, width, color='r')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(rating_values + width / 2)
    ax.set_xticklabels(('1', '2', '3', '4', '5'))


    plt.title("Number of Ratings Across %s Movies" % genre_name)
    plt.xlabel("Rating")
    plt.ylabel("Number of Ratings")


    plt.savefig("visualizations/%s_ratings_bar_chart.pdf" % genre_name)
