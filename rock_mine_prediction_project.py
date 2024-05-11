# -*- coding: utf-8 -*-
"""Rock Mine Prediction Project"""


"""Importing the dependencies"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Preparing the data for the model"""

sonar_data = pd.read_csv('/content/sonar data.csv', header=None)

sonar_data.head()

sonar_data.shape

sonar_data.describe()

sonar_data[60].value_counts()

sonar_data.groupby(60).mean()

#Separating the Data and Labels

x = sonar_data.drop(columns=60, axis=1)
y = sonar_data[60]
print(x)
print(y)

"""Creating trainging and test data"""

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, stratify=y, random_state=1)

print(x.shape, x_train.shape, x_test.shape)

"""Model Trainging: Logistic Regression"""

print(x_train, y_train)

model = LogisticRegression()

#training the model with the training data
model.fit(x_train, y_train)

"""Model Accuracy"""

#training data accuracy
x_training_prediction = model.predict(x_train)
training_data_accuracy = accuracy_score(x_training_prediction, y_train)
print("Accuracy Score of the Model:", training_data_accuracy)

#tests data accuracy
x_test_prediction = model.predict(x_test)
test_data_accuracy = accuracy_score(x_test_prediction, y_test)
print("Accuracy Score of the Model:", test_data_accuracy)

"""Making a Predicitve System"""

#Sample data to test presiction
#input_data = (0.0664,0.0575,0.0842,0.0372,0.0458,0.0771,0.0771,0.1130,0.2353,0.1838,0.2869,0.4129,0.3647,0.1984,0.2840,0.4039,0.5837,0.6792,0.6086,0.4858,0.3246,0.2013,0.2082,0.1686,0.2484,0.2736,0.2984,0.4655,0.6990,0.7474,0.7956,0.7981,0.6715,0.6942,0.7440,0.8169,0.8912,1.0000,0.8753,0.7061,0.6803,0.5898,0.4618,0.3639,0.1492,0.1216,0.1306,0.1198,0.0578,0.0235,0.0135,0.0141,0.0190,0.0043,0.0036,0.0026,0.0024,0.0162,0.0109,0.0079)#R
input_data = [0.0209,0.0261,0.0120,0.0768,0.1064,0.1680,0.3016,0.3460,0.3314,0.4125,0.3943,0.1334,0.4622,0.9970,0.9137,0.8292,0.6994,0.7825,0.8789,0.8501,0.8920,0.9473,1.0000,0.8975,0.7806,0.8321,0.6502,0.4548,0.4732,0.3391,0.2747,0.0978,0.0477,0.1403,0.1834,0.2148,0.1271,0.1912,0.3391,0.3444,0.2369,0.1195,0.2665,0.2587,0.1393,0.1083,0.1383,0.1321,0.1069,0.0325,0.0316,0.0057,0.0159,0.0085,0.0372,0.0101,0.0127,0.0288,0.0129,0.0023]#M

#to convert input_data to numpy array
input_data_np_array = np.asarray(input_data)

#reshape the np array
input_reshaped = input_data_np_array.reshape(1,-1)

prediction = model.predict(input_reshaped)
print(prediction)

if prediction == "R":
  print("Rock")
else:
  print("Mine")