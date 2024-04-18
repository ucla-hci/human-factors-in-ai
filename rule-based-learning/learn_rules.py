from rulekit import RuleKit
from rulekit.classification import RuleClassifier
from sklearn.datasets import load_iris
 
X, y = load_iris(return_X_y=True)
 
print(X, y)

# FIXME: the following does not work on M1 chip
clf = RuleClassifier()
clf.fit(X, y)
prediction = clf.predict(X)
 
print(prediction)