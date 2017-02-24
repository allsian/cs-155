import csv
import random
from collections import Counter


with open('train_2008.csv', 'r') as dest_f:

    data_iter = csv.reader(dest_f, delimiter = ",", quotechar = '"')
    data = [data for data in data_iter]

    # print data[0]
    # print data[1]
    # print data[2]

    labels = data[0]
    data = data[1:]

    age_index = labels.index("PEAGE")
    wealth_index = labels.index("HUFAMINC")




    random.shuffle(data)

    X_train = [map(int, datum[:-1]) for datum in data]
    y_train = [int(datum[-1]) for datum in data]

    cnt_total = Counter()
    cnt_voted = Counter()

    for X, y in zip(X_train, y_train):
        cnt_total[X[age_index], X[wealth_index]] += 1
        if y == 1:
            cnt_voted[X[age_index], X[wealth_index]] += 1

print cnt_total
print cnt_voted




with open('vis.csv', 'wb') as savefile:

    w = csv.writer(savefile, delimiter = ",", quotechar = '"')

    for age in range(18, 80):

        row = []
        for wealth in range(1, 17):
            if cnt_total[age, wealth]:
                row.append(float(cnt_voted[age, wealth])/cnt_total[age, wealth])

            else:
                row.append("x")

        w.writerow(row)
        print row
