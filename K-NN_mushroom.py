# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 00:43:00 2018

@author: DEVIL
"""
#Attribute for dataset
"""
classes: edible=e, poisonous=p (outcome)
cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s
cap-surface: fibrous=f,grooves=g,scaly=y,smooth=s
cap-color: brown=n, buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y
bruises: bruises=t, no=f
odor: almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p,spicy=s
gill-attachment: attached=a,descending=d,free=f,notched=n
gill-spacing: close=c,crowded=w,distant=d
gill-size: broad=b,narrow=n
gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g,
green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y
stalk-shape: enlarging=e,tapering=t
stalk-root: bulbous=b,club=c,cup=u,equal=e,rhizomorphs=z,rooted=r,missing=?
stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s
stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s
stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y
stalk-color-below-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y
veil-type: partial=p,universal=u
veil-color: brown=n,orange=o,white=w,yellow=y
ring-number: none=n,one=o,two=t
ring-type: cobwebby=c,evanescent=e,flaring=f,large=l,none=n,pendant=p,sheathing=s,zone=z
spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r,orange=o,purple=u,white=w,yellow=y
population: abundant=a,clustered=c,numerous=n,scattered=s,several=v,solitary=y
habitat: grasses=g,leaves=l,meadows=m,paths=p,urban=u,waste=w,woods=d """


#Classification on the given dataset to predict if the mushroom is edible or poisonous on basis of habitat, population and odor as the predictors

import pandas as pd
#reading scv file
ds = pd.read_csv('mushrooms.csv')
features = ds.iloc[:, [5,21,22]].values
label = ds.iloc[:, 0:1].values

#feature scaling of data
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
lb = LabelEncoder()
features[:, 0] = lb.fit_transform(features[:, 0])
features[:, 1] = lb.fit_transform(features[:, 1])
features[:, 2] = lb.fit_transform(features[:, 2])
label = lb.fit_transform(label)
#labeled data encoding
onehotencoder = OneHotEncoder(categorical_features = 'all')
features = onehotencoder.fit_transform(features).toarray()
#splitting dataset in train and test
from sklearn.model_selection import train_test_split
f_train, f_test, l_trains, l_test = train_test_split(features, label, test_size = .2, random_state = 0)
#classifing data using KNeighbors regression model
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2)
classifier.fit(f_train, l_trains)
#predicting result for test dataset
l_pred = classifier.predict(f_test)
#confusion matrix for performance of classification model
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(l_test, l_pred)
#score for the model performance
Score = classifier.score(f_test, l_test)