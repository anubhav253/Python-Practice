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

