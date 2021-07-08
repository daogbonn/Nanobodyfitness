# Other Functions to evaluate the models
from sklearn.cluster import KMeans


def clusterpred(train, test, test_true_class, nclusters):
    """Carry out kmeans on the train and predicts test data of interest. Computes n number of clusters and returns
    an array predlo and predhi showing which clusters each of the high or low"""
    kmeans = KMeans(n_clusters=nclusters, init="k-means++")
    kmeans.fit(train)
    sol = kmeans.predict(test)
    predlo = [0]*nclusters  # pred[0] shows the amount of sol[a] that are in cluster 0 that are low fitness
    predhi = [0]*nclusters  # pred[0] shows the amount of sol[a] that are in cluster 0 that are high fitness
    for a in range(len(sol)):  # The length of sol
        for x in range(nclusters):  # The possible clusters: 0, 1, 2, 3
            if sol[a] == x:
                if test_true_class[a] == 0:
                    predlo[x] = predlo[x] + 1
                else:
                    predhi[x] = predhi[x] + 1
    return predlo, predhi
