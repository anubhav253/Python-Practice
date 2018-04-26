# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 18:30:09 2018

@author: DEVIL
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#reading the dataset
data = pd.read_csv('speeding_features.csv')
features = data.iloc[:, [1,2]].values
#classify data using KMeans unsupervised learning
from sklearn.cluster import KMeans
#taking an empty list
wcss = []
#elbow method to find the number of clusters required
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
#plotting the graph and checking where is the maximum deflection    
plt.plot(range(1,11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

#2 clusters are required for this model
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)
y_means = kmeans.fit_predict(features)
#if mean percentage of time a driver was >5 mph over the speed limit then it is driving in Urban area.
plt.scatter(features[y_means == 0, 0], features[y_means == 0,1], s = 100, c = 'red', label = 'Rural')
plt.scatter(features[y_means == 1, 0], features[y_means == 1,1], s = 100, c = 'blue', label = 'Urban')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'green', label = 'Centroids')
plt.xlabel('Distance')
plt.ylabel('Speed')
plt.legend()
plt.show()