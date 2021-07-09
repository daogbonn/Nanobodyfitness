# Looking at Decision Tree Classifier

# Encoding
import numpy
import os.path
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris, load_boston
from sklearn.model_selection import train_test_split
from split_data import split_dataframes_train_test
from sklearn import tree
from sklearn.metrics import confusion_matrix
import graphviz
from IPython.display import Image
from pydot import graph_from_dot_data
from dtreeviz.trees import dtreeviz

a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\test_low_one_hot_encoded_cdrs.csv"
b = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\test_high_one_hot_encoded_cdrs.csv"

train, train_true_class, test, test_true_class = split_dataframes_train_test(a, b, 0.3)

# # Model
# dt = DecisionTreeClassifier()
# dt.fit(train, train_true_class)

# Model
dt = tree.DecisionTreeClassifier()
# gini versus entropy
dt = dt.fit(train, train_true_class)


# Prediction
sol = dt.predict(test)
# Tune hyperparameters of max depth and min leaf size

# See the Decision Tree
tree.plot_tree(dt)
plt.savefig('DecisionTree.pdf')
# pixels per inch to 300
plt.show()

# Another Decision Tree
# try dtreeviz

# Other
# prob for test
proba = dt.predict_proba(train) # 	Predict class probabilities of the input samples X.
print(proba)
# weird that the probabilities are only 1 and 0; if so the success criteria (or percent) should be greater.

# Compute accuracy
true = 0
for a in range(len(sol)):
    if sol[a] == test_true_class[a]:
        true = true + 1
ac = true / len(sol)
print('The Success percent is:', ac * 100, '%')

# Confusion Matrix
conf = confusion_matrix(test_true_class,sol)
print(conf)
suc = (conf[0][0] + conf[1][1])/conf.sum()
print(suc*100, '%')



#  Note
# the Success percent is 58.4285%


# To Do
# Look at the decision tree and recapitulate


