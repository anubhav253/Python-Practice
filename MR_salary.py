# -*- coding: utf-8 -*-
"""
Created on Fri Apr 06 10:12:44 2018

@author: DEVIL
"""

#Multiple linear regression

import pandas as pd
import numpy as np

#taking values from csv file which is salary classifications of employees
dataset = pd.read_csv('Salary_Classification.csv')
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:,-1:].values

#encoding of categoricaldata
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
l_enc = LabelEncoder()
features[:, 0] = l_enc.fit_transform(features[:, 0])

oh_enc = OneHotEncoder(categorical_features = [0])
features = oh_enc.fit_transform(features).toarray()

#avoiding dummy variable
features = features[:, 1:]

#splitting dataset
from sklearn.model_selection import train_test_split
f_train, f_test, l_train, l_test = train_test_split(features, labels, test_size = .2, random_state = 0)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
f_train = sc.fit_transform(f_train)
f_test = sc.transform(f_test)

#Multiple LR fitting for traning data
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(f_train, l_train)

#predicting test data
pred = reg.predict(f_test)

#score for multiple LR model
score = reg.score(f_train, l_train)

