from sklearn import ensemble
import sklearn_classifier

for i in range(25, 1500, 25):
    clf = ensemble.GradientBoostingClassifier(n_estimators=i)
    sklearn_classifier.classify(clf, 'gradientboost/gradientboost-%d' % i)
