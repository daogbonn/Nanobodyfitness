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

a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\combined_clean_aln_low_one_hot_encoded_cdrs.csv"
b = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\combined_clean_aln_high_one_hot_encoded_cdrs.csv"

train, train_true_class, test, test_true_class = split_dataframes_train_test(a, b, 0.3)

# # Model
# dt = DecisionTreeClassifier()
# dt.fit(train, train_true_class)

# Model
dt = tree.DecisionTreeClassifier() # gini versus entropy
dt = dt.fit(train, train_true_class)

print('Depth:', dt.get_depth())
print('Leaf Size', dt.get_n_leaves())

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
#print(proba)
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




# Checking for max depth and accuracy

depth = numpy.linspace(2, 25, num=24).astype(int)
lfsz = numpy.linspace(5, 100, num=10).astype(int)
acc = []
TPR = []
TNR = []
FNR = []
FPR = []
for i in range(len(lfsz)):
    lf = lfsz[i]
    dt = tree.DecisionTreeClassifier(min_samples_leaf=lf, max_depth=14)  # gini versus entropy
    dt = dt.fit(train, train_true_class)
    sol = dt.predict(test)
    tree.plot_tree(dt)
    plt.show()
    true = 0
    conf = confusion_matrix(test_true_class, sol)
    suca = (conf[0][0] + conf[1][1]) / conf.sum()
    TPRa = conf[1][1] / (numpy.sum(conf, 0)[1])
    TNRa = conf[0][0] / (numpy.sum(conf, 0)[0])
    FPRa = conf[1][0] / (numpy.sum(conf, 0)[1])
    FNRa = conf[0][1] / (numpy.sum(conf, 0)[0])
    acc.append(suca)
    TPR.append(TPRa)
    TNR.append(TNRa)
    FNR.append(FNRa)
    FPR.append(FPRa)



plt.plot(lfsz, TPR, 'b')
plt.plot(lfsz, TNR, 'g')
plt.plot(lfsz, acc, 'k')
plt.plot(lfsz, FNR, 'r')
plt.plot(lfsz, FPR, 'y')
labels = 'TPR', 'TNR', 'Accuracy', 'FNR', 'FPR'
plt.legend(labels)
plt.xlabel('Leaf')
plt.ylabel('Rate')
plt.title('Leaf versus Rates - Decision Tree Classifier')
plt.show()

# plt.plot(depth, TPR, 'b')
# plt.plot(depth, TNR, 'g')
# plt.plot(depth, acc, 'k')
# labels = 'TPR', 'TNR', 'Accuracy'
# plt.legend(labels)
# plt.xlabel('Depth')
# plt.ylabel('Rate')
# plt.title('Depth versus Rates - Decision Tree Classifier')
# plt.show()



