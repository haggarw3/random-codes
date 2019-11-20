from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)

X, y = make_blobs(n_samples=1500, n_features =2, centers=7, cluster_std=0.5)

kmeans = KMeans(n_clusters=7)
kmeans.fit(X)
y_pred = kmeans.predict(X)

plt.figure(figsize=(6,6))
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='hsv')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=25, alpha=0.75)

plt.show()

