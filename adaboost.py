from sklearn import ensemble
from sklearn import tree
import sklearn_classifier

for i in range(25, 1500, 25):
    clf = ensemble.AdaBoostClassifier(n_estimators=i)
    sklearn_classifier.kfold_classify(clf, 'adaboost/adaboost-%d' % i)
