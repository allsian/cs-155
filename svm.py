import format_data
from sklearn.svm import SVC

def error(expected, actual):
  count = 0
  for idx in range(len(expected)):
    if expected[idx] != actual[idx]:
      count += 1

  return float(count) / len(expected)

print "CCC"

X_train, y_train, X_test, y_test = format_data.get_formatted_data()

clf = SVC()
print "Aaa"
clf.fit(X_train, y_train)
print "Bbb"
eout = error(y_test, clf.predict(X_test))
ein = error(y_train, clf.predict(X_train))
print ein
print eout
