import format_data
import csv
from sklearn import ensemble

def error(expected, actual):
    count = 0
    for idx in range(len(expected)):
        if expected[idx] != actual[idx]:
            count += 1

    return float(count) / len(expected)

X_train, y_train, X_val, y_test, X_test = format_data.get_formatted_data()

for i in range(1, 10):
    clf = ensemble.RandomForestClassifier(n_estimators=50, max_features=None, min_samples_leaf=i)
    clf.fit(X_train, y_train)

    eout = error(y_test, clf.predict(X_val))
    ein = error(y_train, clf.predict(X_train))
    test_results = clf.predict(X_test)

    with open('random-forest-%d.csv' % i, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        writer.writerow(['id', 'PES1'])
        for idx, prediction in enumerate(test_results):
            writer.writerow([idx, prediction + 1])
    print 'stats for i = %d:' % i
    print ein
    print eout