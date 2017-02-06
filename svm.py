import sklearn_classifier
from sklearn.svm import SVC

clf = SVC(kernel='linear', C=0.5)
sklearn_classifier.classify(clf, 'svm/svm')
