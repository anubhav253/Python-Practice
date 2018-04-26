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
    
plt.plot(range(1,11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()