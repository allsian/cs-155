import format_data
import csv
from sklearn import ensemble
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score



def error(expected, actual):
    count = 0
    for idx in range(len(expected)):
        if expected[idx] != actual[idx]:
            count += 1

    return float(count) / len(expected)

def classify(clf, clf_string):
    X_train, y_train, X_val, y_val, X_test = format_data.get_formatted_data()

    clf.fit(X_train, y_train)

    eout = error(y_test, clf.predict(X_val))
    ein = error(y_train, clf.predict(X_train))
    test_results = clf.predict(X_test)

    with open('output/%s.csv' % clf_string, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        writer.writerow(['id', 'PES1'])
        for idx, prediction in enumerate(test_results):
            writer.writerow([idx, prediction + 1])
    print 'stats for %s:' % clf_string
    print 'ein', 1 - ein
    print 'eout', 1 - eout


def kfold_classify(clf, clf_string):
    X_train, y_train = format_data.get_unsplit_data()


    scores = cross_val_score(clf, X_train, y_train, cv=5)
    print scores
