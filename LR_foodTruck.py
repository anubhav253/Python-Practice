# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 04:22:06 2018

@author: DEVIL
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#reading csv file
dataset = pd.read_csv("Foodtruck.csv")
#defining dependent and independent variables
features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,-1].values
#splitting the dataset
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels, test_size=0.2, random_state=0)
#using linear regression algo
from sklearn.linear_model import LinearRegression
re = LinearRegression()
re.fit(features_train,labels_train)
#predicting profits for test data
labels_pred = re.predict(features_test)
#plotting the graph
plt.scatter(features_train, labels_train, color='blue')
plt.scatter(features_test, labels_test, color='green')
plt.plot(features_train, re.predict(features_train),color='red')
plt.title("Population vs Profit")
plt.xlabel("Population")
plt.ylabel("Profit")
plt.show()
#predicting profit or loss on the basis of population 
labels_pred1 = re.predict(3.073)