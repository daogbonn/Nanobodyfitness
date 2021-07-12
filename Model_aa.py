# Combine all the models used

# Models - Kmeans, Logistic Regression, Decision Tree Classifier, Neural Network

# Import
import numpy
import os.path
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.datasets import load_iris, load_boston
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from split_data import split_dataframes_train_test

import graphviz
from IPython.display import Image
from pydot import graph_from_dot_data
from dtreeviz.trees import dtreeviz

from model_functions import clusterpred


# Import Data

a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\combined_clean_aln_low_one_hot_encoded_cdrs.csv"
b = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\combined_clean_aln_high_one_hot_encoded_cdrs.csv"

train, train_true_class, test, test_true_class = split_dataframes_train_test(a, b, 0.3)
nmodels = 4
sucmat = [0]*nmodels
trupos = [0]*nmodels
truneg = [0]*nmodels
names = ['Kmeans Cluster', 'Decision Tree', 'Logistic Regression', 'Neural Network']

# KMeans _ Clustering
kmeans = KMeans(n_clusters=2, init="k-means++")
kmeans.fit(train)
sol = kmeans.predict(test)
conf = confusion_matrix(test_true_class,sol)
suc = (conf[0][0] + conf[1][1])/conf.sum()
TPR = conf[1][1]/(numpy.sum(conf,0)[1])
TNR = conf[0][0]/(numpy.sum(conf,0)[0])
sucmat[0] = suc
trupos[0] = TPR
truneg[0] = TNR

# Decision Tree Classifier
dt = tree.DecisionTreeClassifier(min_samples_leaf=50, max_depth=14)
dt = dt.fit(train, train_true_class)
sol = dt.predict(test)
conf = confusion_matrix(test_true_class,sol)
suc = (conf[0][0] + conf[1][1])/conf.sum()
TPR = conf[1][1]/(numpy.sum(conf,0)[1])
TNR = conf[0][0]/(numpy.sum(conf,0)[0])
print(suc*100, '%')
sucmat[1] = suc
trupos[1] = TPR
truneg[1] = TNR
tree.plot_tree(dt)
plt.savefig('DecisionTreeLong.pdf')
plt.show()

# Logistic Regression
lr = LogisticRegression().fit(train, train_true_class)
sol = lr.predict(test)
sc = lr.score(test, test_true_class) # Same as accuracy below
conf = confusion_matrix(test_true_class,sol)
suc = (conf[0][0] + conf[1][1])/conf.sum()
TPR = conf[1][1]/(numpy.sum(conf,0)[1])
TNR = conf[0][0]/(numpy.sum(conf,0)[0])
print(suc*100, '%')
sucmat[2] = suc
trupos[2] = TPR
truneg[2] = TNR

# Neural Network
nn = MLPClassifier().fit(train, train_true_class)
sol = nn.predict(test)
conf = confusion_matrix(test_true_class,sol)
suc = (conf[0][0] + conf[1][1])/conf.sum()
TPR = conf[1][1]/(numpy.sum(conf,0)[1])
TNR = conf[0][0]/(numpy.sum(conf,0)[0])
print(suc*100, '%')
sucmat[3] = suc
trupos[3] = TPR
truneg[3] = TNR

# Plot of success
plt.plot(names, sucmat)
plt.xlabel('Models Used')
plt.ylabel('Accuracy (%)')
plt.title('Plot of models versus Accuracy')
plt.show()

# Plot of positive and negative rates
plt.plot(names, trupos, 'b')
plt.plot(names, truneg, 'g')
plt.plot(names, sucmat, 'k')
labels = 'TPR', 'TNR', 'Accuracy'
plt.legend(labels)
plt.xlabel('Models Used')
plt.ylabel('Rate')
plt.show()

# Other things to graph together
# probability using proba




