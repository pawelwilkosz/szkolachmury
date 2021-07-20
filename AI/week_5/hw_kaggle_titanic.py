# Reading data 
import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn import tree

train_dataset = pd.read_csv("train.csv", header=0);
test_dataset = pd.read_csv("test.csv", header=0);

# Preparing Data
train_dataset = train_dataset.fillna(0)
test_dataset = test_dataset.fillna(0)

X = train_dataset.iloc[:, [0,2,4,5,6,7]]
Y = train_dataset.iloc[:, 1]

X_test = test_dataset.iloc[:, [0,1,3,4,5,6]]

X2 = pd.get_dummies(X)
X2_test = pd.get_dummies(X_test)

# Apply model
model = tree.DecisionTreeClassifier(max_depth=6)

# Train Model
model.fit(X2, Y)

# Prediction and evaluationues
y_predict = model.predict(X2_test)
y_predict

f = open("Result.csv", 'w')

for x in range(0,417):
   # f.write('' + X2_test["PassengerId"][x]+','+y_predict[x])
    test = (str(X2_test["PassengerId"][x]) + ',' + str(y_predict[x]))
    f.write(test)
    f.write('\n')

f.close()