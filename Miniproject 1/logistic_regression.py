import sklearn_classifier
from sklearn.linear_model import LogisticRegression


clf = LogisticRegression()
sklearn_classifier.classify(clf, 'linear-regression.csv')