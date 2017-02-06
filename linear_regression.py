import format_data
from sklearn.linear_model import LinearRegression

def error(expected, actual):
  count = 0
  for idx in range(len(expected)):
    if expected[idx] != actual[idx]:
      count += 1

  return float(count) / len(expected)

X_train, y_train, X_test, y_test = format_data.get_formatted_data()

clf = LinearRegression()
clf.fit(X_train, y_train)

test_predicted = clf.predict(X_test)
train_predicted = clf.predict(X_train)
print test_predicted[0:20]
print y_test[0:20]
eout = error(y_test, test_predicted)
ein = error(y_train, train_predicted)
print ein
print eout