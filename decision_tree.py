import get_data
from sklearn import tree

def error(expected, actual):
    count = 0
    for idx in range(len(expected)):
        if expected[idx] != actual[idx]:
            count += 1

    return float(count) / len(expected)

X_train, y_train, X_test, y_test = get_data.get_data()

clf = tree.DecisionTreeClassifier()
clf.fit(X_train, y_train)

eout = error(y_test, clf.predict(X_test))
ein = error(y_train, clf.predict(X_train))
print ein
print eout