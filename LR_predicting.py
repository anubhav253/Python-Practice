# -*- coding: utf-8 -*-
"""
Created on Fri Apr 06 09:38:22 2018

@author: DEVIL
"""

import matplotlib.pyplot as plt
import pandas as pd

#taking values from csv file
dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')
#defining dependent and independent variables
features = dataset.iloc[:, 0:1].values
labels_bahu = dataset.iloc[:,1:2].values
labels_dangal = dataset.iloc[:,2:3].values

#using algo and fitting the data
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features, labels_bahu)
regressor2 = LinearRegression()
regressor2.fit(features, labels_dangal)