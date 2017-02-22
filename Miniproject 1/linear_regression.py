import sklearn_classifier
from sklearn.linear_model import LinearRegression


clf = LinearRegression()
sklearn_classifier.classify(clf, 'linear-regression.csv')