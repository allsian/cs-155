from sklearn import ensemble
import sklearn_classifier

for i in range(100, 1500, 100):
    clf = ensemble.AdaBoostClassifier(n_estimators=i)
    sklearn_classifier.classify(clf, 'adaboost/adaboost-%d' % i)
