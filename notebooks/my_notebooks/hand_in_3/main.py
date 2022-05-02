from sklearn.datasets import load_wine
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn import metrics
import pandas as pd
import matplotlib as mpl
import numpy as np
import pandas as pd
import seaborn as sb
# reset defaults because we change them further down this notebook
mpl.rcParams.update(mpl.rcParamsDefault)
import matplotlib.pyplot as plt


wine = load_wine()

df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['target'] = wine.target
print(wine.target)


def mean_shift(data, n_samples=1000):
    bandwidth = estimate_bandwidth(data, quantile=0.33, n_samples=n_samples)

    ms = MeanShift(bandwidth=bandwidth,  bin_seeding=True) # can be used to speed up process, since fewer kernels are created.
    ms.fit(data)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters = len(labels_unique)

    print('Number of estimated clusters : {}'.format(n_clusters))
    
    return labels, cluster_centers, n_clusters


labels, cluster_centers, n_clusters = mean_shift(df)
print(cluster_centers)
print(type(labels))
print(wine.target)
print(labels)
print(n_clusters)

#best silhouette score
rand_score = metrics.adjusted_rand_score(wine.target, labels)
silhouette_score = metrics.silhouette_score(wine.data, labels)
print(rand_score)
print(silhouette_score)
print(df.head())
print(df.corr())

mpl.use("Agg")
#mpl.style.use('ggplot')
sb_plot = sb.pairplot(df, hue="target", height=2.5)
plt.savefig("output.pdf")
