import get_data
from sklearn import ensemble

def error(expected, actual):
  count = 0
  for idx in range(len(expected)):
    if expected[idx] != actual[idx]:
      count += 1

  return float(count) / len(expected)

X_train, y_train, X_test, y_test = get_data.get_data()

clf = ensemble.RandomForestClassifier()
clf.fit(X_train, y_train)

eout = error(y_test, clf.predict(X_test))
print eout