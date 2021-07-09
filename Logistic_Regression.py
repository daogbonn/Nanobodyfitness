# Looking at Logistic Regression Classifier

# Encoding
import numpy
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from split_data import split_dataframes_train_test
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import graphviz
from IPython.display import Image
from pydot import graph_from_dot_data
from dtreeviz.trees import dtreeviz

a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\test_low_one_hot_encoded_cdrs.csv"
b = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\test_high_one_hot_encoded_cdrs.csv"

train, train_true_class, test, test_true_class = split_dataframes_train_test(a, b, 0.3)


# Model
lr = LogisticRegression().fit(train, train_true_class)

# Prediction
sol = lr.predict(test)

# Other Calculations
proba = lr.predict_proba(test) # Shows the probability of it being one or another
sc = lr.score(test, test_true_class) # Same as accuracy below

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

# Better - 68% accuracy