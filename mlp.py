from sklearn import ensemble
from sklearn import tree
import sklearn_classifier
from sklearn.neural_network import MLPClassifier


for i in range(100, 1500, 200):
    print 'mlp, i = ', i
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(i, 2), random_state=1)
    sklearn_classifier.kfold_classify(clf, 'mlp/mlp-%d' % i)
