# Better scoring model

import pandas
from sklearn.model_selection import train_test_split
from sklearn import tree

df = pandas.read_csv("Churn_Modelling.csv", sep=",", header=0);
df.head()

X = df.iloc[:,0:12]
Y = df.iloc[:,13]

X2 = pandas.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(X2, Y, random_state=1)

model = tree.DecisionTreeClassifier(max_depth=6)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
model.score(X_test, y_test)