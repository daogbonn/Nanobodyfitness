# Goal - Model using Neural Networks

# Encoding
import numpy
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from split_data import split_dataframes_train_test
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import confusion_matrix

a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\test_low_one_hot_encoded_cdrs.csv"
b = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\test_high_one_hot_encoded_cdrs.csv"

train, train_true_class, test, test_true_class = split_dataframes_train_test(a, b, 0.3)


# Model
nn = MLPClassifier().fit(train, train_true_class)

# Prediction
sol = nn.predict(test)

# Other Calculations
proba = nn.predict_proba(test) # Shows the probability of it being one or another
sc = nn.score(test, test_true_class) # Same as accuracy below
print('Prob:', proba, 'accuracy:', sc)

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

# Accuracy - 68%