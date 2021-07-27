# Text analytics with prediction model for a single value

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

dataset = pd.read_csv('M9L3-Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)
dataset.head()

corpus = []

for i in range(0, 1000): 
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

corpus

cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

# Single value prediction

cv1 = CountVectorizer(max_features = 1500)

pred = 'So bad food'
corpus1=[]

review1 = re.sub('[^a-zA-Z]', ' ', pred)
review1 = review1.lower()
review1 = review1.split()
ps1 = PorterStemmer()
review1 = [ps1.stem(word) for word in review1 if not word in set(stopwords.words('english'))]
review1 = ' '.join(review1)
corpus1.append(review1)

test_vec = cv.transform(corpus1)
y2_pred = classifier.predict(test_vec.toarray())

y2_pred