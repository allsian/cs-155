from sklearn import ensemble
import sklearn_classifier

for i in range(25, 1500, 25):
    clf = ensemble.AdaBoostClassifier(n_estimators=i)
    sklearn_classifier.classify(clf, 'adaboost/adaboost-%d' % i)
