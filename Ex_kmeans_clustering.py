import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


# Generate Synthetic data and labels
features, true_labels = make_blobs(n_samples=200, centers=3, cluster_std=2.75, random_state=42)
print(features[:5])
print(true_labels[:5])

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

print(scaled_features[:5])
print(true_labels[:5])

#Instantiate the KMeans class
kmeans = KMeans(init="random",  n_clusters=3, n_init=10, max_iter=300, random_state=42)
kmeans.fit(scaled_features)

# Attributes of kmeans
print('The lowest SSE value:', kmeans.inertia_) #The lowest SSE value
print('Final locations of the centroid: \n', kmeans.cluster_centers_)
print('The number of iterations required to converge: ', kmeans.n_iter_)

# predicted labels of the first five
print(kmeans.labels_[:5])

# Plot
kmeans_kwargs = {"init": "random", "n_init": 10, "max_iter": 300, "random_state": 42}
# A list holds the SSE values for each k
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    kmeans.fit(scaled_features)
    sse.append(kmeans.inertia_)

plt.style.use("fivethirtyeight")
plt.plot(range(1, 11), sse)
plt.xticks(range(1, 11))
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.tight_layout()
plt.show()


# Find the right number of clusters needed to find the right amount of clusters
# First -  Elbow Method
kl = KneeLocator(range(1, 11), sse, curve="convex", direction="decreasing")
print('The right number of clusters:', kl.elbow)

# Second - Silhouette Coefficient
silhouette_coefficients = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    kmeans.fit(scaled_features)
    score = silhouette_score(scaled_features, kmeans.labels_)
    silhouette_coefficients.append(score)

plt.style.use("fivethirtyeight")
plt.plot(range(2, 11), silhouette_coefficients)
plt.xticks(range(2, 11))
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Coefficient")
plt.tight_layout()
plt.show()

# Note - Higher silhouette coefficient = elbow point (or knee point)

