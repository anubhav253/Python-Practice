# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 00:05:26 2018

@author: DEVIL
"""

import pandas as pd

am = pd.read_csv('Automobile.csv')
new_data = pd.DataFrame()

for i in am:
    if am[i].dtype == object:
        new_data[i] = am[i]

