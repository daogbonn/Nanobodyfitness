# Goal - to use kmeans to train and test the data

# Encoding
import numpy
import os.path
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from split_data import split_dataframes_train_test
from sklearn.metrics import confusion_matrix
from model_functions import clusterpred

a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\test_low_one_hot_encoded_cdrs.csv"
b = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\test_high_one_hot_encoded_cdrs.csv"

train, train_true_class, test, test_true_class = split_dataframes_train_test(a, b, 0.3)

# Scale the feautures
scaler = StandardScaler()
scaled = scaler.fit_transform(train)

# Training
kmeans = KMeans(n_clusters=2, init="k-means++")
kmeans = kmeans.fit(train) #kmeans = kmeans.fit(train)
# Attributes of kmeans
print('The lowest SSE value:', kmeans.inertia_)  # The lowest SSE value
print('Final locations of the centroid: \n', kmeans.cluster_centers_)
print('The number of iterations required to converge: ', kmeans.n_iter_)
# Prediction
sol = kmeans.predict(test)
sola = kmeans.fit_predict(test) # fits and predicts the data

diff = 0
for a in range(len(sol)):
    if sol[a] == sola[a]:
        diff = diff+1

print(diff)
print(len(sol)-diff)
print(len(sola))
print(len(sol))


# Compute accuracy
true = 0
for a in range(len(sol)):
    if sola[a] == test_true_class[a]:
        true = true + 1
ac = true / len(sol)
print('The Success percent is:', ac * 100, '%')

true = 0
for a in range(len(sol)):
    if sol[a] == test_true_class[a]:
        true = true + 1
ac = true / len(sol)
print('The Success percent is:', ac * 100, '%')

# Confusion Matrix (same as above)
conf = confusion_matrix(test_true_class,sol)
print(conf)
suc = (conf[0][0] + conf[1][1])/conf.sum()
print(suc*100, '%')


# looking at more than two clusters
predlo, predhi = clusterpred(train, test, test_true_class, 4)
print(predlo, predhi)
# TD - Make a sequence logo out of the sequences and see what makes up the clusters and the differences
# Need a way to evaluate the clusters and also compute the success percent


# Plotted to see the number of clusters and it seems like the larger the number of clusters the lower the SSE is
# Using scaled versus train in kmeans.fit
# If Scaled is used - smaller amount of iterations needed to converge, higher SSE
# Scaled: SSE - 94572.35; # of iterations - 2
# Test: SSE - 4032.95; # of iterations - 7
# Success % - 56.375 % when raw success is computed using train; 46.625 % using scaled
# When you run multiple times it ranges from 56 to 43%
# Confusion Matrix - [0,0] - true negatives; [1,0] - false negatives; [1,1] - true positives, [0,1] - false positives
# [[true neg, false pos] [false neg, true pos]]

# Question - fit_predict and predict are not the same thing; what is the diff
# Is there a way to see the probability of the clusters?

# to do
# - Plot the SSE versus no of clusters for both train and scaled and see

