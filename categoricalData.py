# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 17:04:48 2018

@author: DEVIL
"""
import pandas as pd

data = pd.read_csv('Cricket_2017.csv')
features = data.iloc[:,:-1].values
labels = data.iloc[:, -1].values

#Encoding

from sklearn.preprocessing import OneHotEncoder, LabelEncoder
lb = LabelEncoder()
features[:, 0] = lb.fit_transform(features[:, 0])
features[:, 1] = lb.fit_transform(features[:, 1])

#for labeled data
onehotencoder = OneHotEncoder(categorical_features = [0, 1])
features = onehotencoder.fit_transform(features).toarray()

labels = lb.fit_transform(labels)

from sklearn.model_selection import train_test_split
features_train, features_test, labels_trains, labels_test = train_test_split(features, labels, test_size = .2, random_state = 0)