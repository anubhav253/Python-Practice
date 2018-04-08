# -*- coding: utf-8 -*-
"""
Created on Sun Apr 08 21:24:42 2018

@author: DEVIL
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#reading data from csv file
dataset = pd.read_csv('affairs.csv')
#dependent and independent variables 
features = dataset.iloc[:, :8].values
labels = dataset.iloc[:, -1].values