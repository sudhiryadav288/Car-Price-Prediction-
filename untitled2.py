# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uxSiO1I450F3IBQ4wAGrVweQKBF22spt

Importing Libraries
"""

import numpy as np
import pandas as pd

"""Importing data"""

dataset = pd.read_csv('audi.csv')
x = dataset.iloc[:,[0,1,3,4,5,6,7,8]].values
y = dataset.iloc[:,[2]].values

print(x)

print(y)

"""# `**Data Preprocessing**`

Label Encoding
"""

from sklearn.preprocessing import LabelEncoder
le1 = LabelEncoder()
x[:,0] = le1.fit_transform(x[:,0])
le2 = LabelEncoder()
x[:,4] = le2.fit_transform(x[:,4])

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer(transformers = [('encoder', OneHotEncoder(),[2])],remainder = 'passthrough')
x = ct.fit_transform(x)

print(x)

"""# **Feature Scaling**"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x = sc.fit_transform(x)

print(x)

"""# **Splitting the dataset into training and test set**"""

from sklearn.model_selection import train_test_split
(X_train, X_test, Y_train, Y_test) = train_test_split(x,y,test_size = 0.2, random_state = 0)

"""# Training Model"""

from sklearn.ensemble import RandomForestRegressor
regression = RandomForestRegressor(random_state = 0)
regression.fit(X_train, Y_train)

y_pred = regression.predict(X_test)

print(y_pred)

print(Y_test)

"""Testing Result"""

mydata = np.concatenate((y_pred.reshape(len(y_pred), 1), Y_test.reshape(len(Y_test), 1)),1)

"""## Calculateing Accuracy"""

from sklearn.metrics import r2_score
r2_score(Y_test,  y_pred)

"""# Making Dataframe"""

dataframe = pd.DataFrame(mydata, columns = ['Predicted value','Real Value'])

print(dataframe)

