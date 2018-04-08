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
#labeled data OneHotEncoding
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [6,7])
features = onehotencoder.fit_transform(features).toarray()
features2 = features[:, [1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17]]
#splitting dataset into train(80%) and test(20%)
from sklearn.model_selection import train_test_split
features_train, features_test, labels_trains, labels_test = train_test_split(features2, labels, test_size = .2, random_state = 0)
#classify the dataset using logistic regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(features_train, labels_trains)
#predicting values for test data 1=true and 0=False
labels_pred = classifier.predict(features_test)
#confusion matrix for performance of classification model
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
#score of the model
score = classifier.score(features_test, labels_test)

#to find number of womens with affair
i = 0
count = 0

while i < 6366:
    if dataset["affair"][i] == 1:
        count+=1
    i+=1
#number of womens with affairs and percentage
print count
print (float(count)/6366)*100
#for a random women of age=25,yrs_married=3, has 1 child, a 0ccu=4,educ=16, hus_occu=3 
predict = np.array([0,0,1,0,0,1,0,0,0,0,3,25,3,1,4,16]).reshape(1,-1)
#predicting if she had affair
pred = classifier.predict(predict)