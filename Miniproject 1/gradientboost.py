from sklearn import ensemble
import sklearn_classifier

for i in range(700, 800, 100):
    print 'i is', i
    clf = ensemble.GradientBoostingClassifier(n_estimators=i)
    sklearn_classifier.classify(clf, 'gradientboost/gradientboost-%d' % i)
    #sklearn_classifier.kfold_classify(clf, 'gradientboost/gradientboost-%d' % i)
