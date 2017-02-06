from sklearn import tree
import sklearn_classifier


clf = tree.DecisionTreeClassifier()
sklearn_classifier.classify(clf, 'decision-tree.csv')
