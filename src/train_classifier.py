"""This module trains the classifier with predefined data"""
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np


data_dict = pickle.load(open('./data.pickle', 'rb'))

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])
"""Accessing the data"""

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)
"""Splitting the data into traina and test set"""

model = RandomForestClassifier()
model.fit(x_train, y_train)
y_predict = model.predict(x_test)
"""Training the classifier"""

score = accuracy_score(y_predict, y_test)
print('{}% of samples were classified correctly !'.format(score * 100))
"""Checking the accuracy"""

f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()
