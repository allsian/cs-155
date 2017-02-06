
import sklearn_classifier
from sklearn import ensemble


for i in range(1, 100, 5):
    clf = ensemble.RandomForestClassifier(n_estimators=50, max_features=None, min_samples_leaf=i)

    sklearn_classifier.classify(clf, 'random-forest/random-forest-%i.csv' % i)
