# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt
import heapq
from matplotlib import cm
from operator import add

class MovieHeap(object):
    def __init__(self, max_size):
        self._queue = []
        self.max_size = max_size

    def push(self, movie_id, value):
        if len(self._queue) < self.max_size:
            heapq.heappush(self._queue, (value, movie_id))
        elif self._queue[0][0] < value:
            heapq.heappop(self._queue)
            heapq.heappush(self._queue, (value, movie_id))

    def pop(self):
        return heapq.heappop(self._queue)[1]

    def get_all(self):
        return [element[1] for element in self._queue]

data = np.genfromtxt('project3data/data.txt', delimiter='\t')
movie_info = np.genfromtxt('project3data/movies.txt', delimiter='\t', dtype=str)
movie_ratings = {}

for row in data:
    movie_id = row[1]
    rating = row[2]
    if movie_id not in movie_ratings:
        movie_ratings[movie_id] = [rating]
    else:
        movie_ratings[movie_id].append(rating)

# get 10 most rated movies
popularity_heap = MovieHeap(10)
for movie_id in movie_ratings.keys():
    popularity_heap.push(movie_id, len(movie_ratings[movie_id]))

most_popular_ids = popularity_heap.get_all()
print most_popular_ids

ones = [movie_ratings[movie_id].count(1) for movie_id in most_popular_ids]
twos = [movie_ratings[movie_id].count(2) for movie_id in most_popular_ids]
threes = [movie_ratings[movie_id].count(3) for movie_id in most_popular_ids]
fours = [movie_ratings[movie_id].count(4) for movie_id in most_popular_ids]
fives = [movie_ratings[movie_id].count(5) for movie_id in most_popular_ids]
print [movie_info[movie_id - 1][1] for movie_id in most_popular_ids]

N = 10

ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence
colors = cm.rainbow(np.linspace(0, 1, 5))
p1 = plt.bar(ind, ones, width, color=colors[0], label='1')
p2 = plt.bar(ind, twos, width, bottom=ones, color=colors[1], label='2')
p3 = plt.bar(ind, threes, width, bottom=[sum(ratings) for ratings in zip(ones, twos)], color=colors[2], label='3')
p4 = plt.bar(ind, fours, width, bottom=[sum(ratings) for ratings in zip(ones, twos, threes)], color=colors[3], label='4')
p5 = plt.bar(ind, fives, width, bottom=[sum(ratings) for ratings in zip(ones, twos, threes, fours)], color=colors[4], label='5')

plt.ylabel('Number of Ratings')
plt.title('Ratings for 10 Most Popular Movies')
plt.xticks(ind, [movie_info[movie_id - 1][1] for movie_id in most_popular_ids], rotation=20, fontsize=8)
plt.legend(loc='upper left', ncol=5)
plt.savefig('visualizations/most-popular.png', figsize=(8, 20))
plt.show()