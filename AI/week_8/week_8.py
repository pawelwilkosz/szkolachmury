
import pandas
df = pandas.read_csv("Tweets.csv", header=0, sep=",")

df = df[['airline_sentiment', 'text']]
df.head()

import re

def norm1(row):
    return re.sub("[-()\"#/@;:<>{}`+=~|.!?,]",'', row['text'])
    
df['norm'] = df.apply(norm1, axis=1)
df.head()


sentiment_map = {
    'positive': 1,
    'neutral': 0,
    'negative': -1
}
df['sentiment'] = df['airline_sentiment'].map(sentiment_map)
df.head()


from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(binary=True)
norm = df['norm']
cv.fit(norm)
X = cv.transform(norm)
y = df[['sentiment']]
X.shape

from keras.utils import to_categorical
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y)

num_classes = 3

y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

from keras import models
from keras.layers import Dense, Dropout

model = models.Sequential()
model.add(Dense(100, activation='relu', input_shape=(16529,)))
model.add(Dropout(0.2))
model.add(Dense(100, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='sigmoid'))
model.summary()

model.compile(
 optimizer = "adam",
 loss = "binary_crossentropy",
 metrics = ["accuracy"]
)

results = model.fit(
 X_train, y_train,
 epochs = 2,
 batch_size = 128,
 validation_data = (X_test, y_test)
)

score = model.evaluate(X_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])


