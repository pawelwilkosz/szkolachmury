import pandas
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

df = pandas.read_csv("Churn_Modelling.csv", sep=",", header=0);

df.head()
df.describe()

X = df.iloc[:,0:12]
Y = df.iloc[:,13]
X2 = pandas.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(X2, Y, random_state=1)

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

mlp = MLPClassifier(hidden_layer_sizes=(11))
mlp.fit(X_train,y_train)
mlp.score(X_test, y_test)