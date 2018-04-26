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