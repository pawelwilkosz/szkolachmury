# Reading data'
import pandas
df = pandas.read_csv('M4L5.csv')
df.head()
# df['State'].unique()

# Data preparation
stateMap = {
    'New York': 1,
    'California': 2,
    'Florida': 3
}
df['State Number'] = df['State'].map(stateMap)
normalized_df = df.drop(['State'], axis=1)
normalized_df.head()

# Divide data into test and train
from sklearn.model_selection import train_test_split

X_ben = normalized_df[['R&D Spend', 'Administration', 'Marketing Spend','State Number']]
Y_ben = normalized_df[['Profit']]

Xtrain, Xtest, Ytrain, Ytest = train_test_split(X_ben, Y_ben, random_state=1)

# Apply model
from sklearn import linear_model
regr = linear_model.LinearRegression()

# Train model
regr.fit(Xtrain, Ytrain)

# Prediction on test data
y_pred = regr.predict(Xtest)

# Result
from sklearn.metrics import mean_squared_error

print('Coef: ', regr.coef_)
print('intercept: ', regr.intercept_)
print('Squared error: ', mean_squared_error(Ytest, y_pred))
print('R^2 score: ', regr.score(Xtrain, Ytrain))