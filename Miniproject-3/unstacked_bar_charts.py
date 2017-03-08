

import numpy as np
import matplotlib.pyplot as plt


data = np.transpose(np.genfromtxt('project3data/data.txt', delimiter = '\t', dtype=None))

user_ids_vector = list(data[0])
movie_ids_vector = list(data[1])
rating_vector = list(data[2])



rating_values = np.arange(1, 5+1)

rating_counts = [rating_vector.count(r) for r in rating_values]


print rating_values
print rating_counts

width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(rating_values, rating_counts, width, color='r')

# women_means = (25, 32, 34, 20, 25)
# women_std = (3, 5, 2, 3, 3)
# rects2 = ax.bar(ind + width, women_means, width, color='y', yerr=women_std)

# add some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(rating_values + width / 2)
ax.set_xticklabels(('1', '2', '3', '4', '5'))

# ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))


# def autolabel(rects):
#     """
#     Attach a text label above each bar displaying its height
#     """
#     for rect in rects:
#         height = rect.get_height()
#         ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
#                 '%d' % int(height),
#                 ha='center', va='bottom')
#
# autolabel(rects1)

plt.title("Number of Ratings Across all Movies")
plt.xlabel("Rating")
plt.ylabel("Number of Ratings")


plt.savefig("visualizations/all_ratings_bar_chart.pdf")
