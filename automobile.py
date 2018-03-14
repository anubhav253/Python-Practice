# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 00:05:26 2018

@author: DEVIL
"""

import pandas as pd

am = pd.read_csv('Automobile.csv')
new_data = pd.DataFrame()

#object datatype column in one dataframe
for i in am:
    if am[i].dtype == object:
        new_data[i] = am[i]

#missing values
new_data["num_doors"] = new_data['num_doors'].fillna(new_data['num_doors'].mode()[0])

lst = ["convertible", "hardtop", "hatchback", "sedan", "wagon"]
v = 0

for i in lst:
    new_data["body_style"][new_data["body_style"] == i] = v
    v += 1