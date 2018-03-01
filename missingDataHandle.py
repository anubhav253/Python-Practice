# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 17:21:46 2018

@author: DEVIL
"""

import pandas as pd
from sklearn.preprocessing import Imputer
dataset = pd.read_csv('cars.csv')

x = dataset.iloc[:, 0:2].values
imputer = Imputer(missing_values='NaN', strategy='median',axis=0)
imputer = imputer.fit(x[:, 1:2])
x[:, 1:2] = imputer.transform(x[:, 1:2])

df = pd.DataFrame(x)
df.to_csv('Test2.csv',index= False)