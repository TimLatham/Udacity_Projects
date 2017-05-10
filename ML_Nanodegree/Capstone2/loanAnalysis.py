# -*- coding: utf-8 -*-
"""
Created on Wed May 10 11:39:08 2017

@author: tim.latham
"""

# Import libraries
import numpy as np
import pandas as pd
from time import time
from sklearn.metrics import f1_score
from IPython.display import display
#%matplotlib inline

# Read student data
loan_data = pd.read_csv("loan_data.csv")
print ("Loan data read successfully!")

display(loan_data.head())
print(loan_data.dtypes)

# TODO: Calculate number of records
n_loans = float(len(loan_data))

# TODO: Calculate number of features
n_features = float(len(loan_data.columns) - 1)

# TODO: Calculate paid in full loans
n_pif = float(sum(1 for item in loan_data['loan_status'] if item==(0)))

# TODO: Calculate charged off loans
n_chargeoff = float(sum(1 for item in loan_data['loan_status'] if item==(1)))

# TODO: Calculate successful loan rate
success_rate = n_pif / n_loans * 100

# Print the results
print("Total number of loans: {}".format(n_loans))
print("Number of features: {}".format(n_features))
print("Number of loans paid in full: {}".format(n_pif))
print("Number of charge-offs: {}".format(n_chargeoff))
print("Success rate of loans: {:.2f}%".format(success_rate))

# Store the 'loan_status' feature in a new variable and remove it from the dataset
y_all = loan_data['loan_status']
X_all = loan_data.drop(['loan_status'], axis = 1)

# Show the new dataset with 'loan_status' removed
display(X_all.head())
display(y_all.head())

display(X_all.describe())

X_all = pd.get_dummies(X_all, columns=['home_ownership', 'purpose', 'verification_status'])

display(X_all.head())

quant_features = ['annual_inc', 'collections_12_mths_ex_med', 'delinq_2yrs', 'dti', 'emp_length', 'funded_amnt',
                 'inq_last_6mths', 'installment', 'mths_since_last_delinq', 'mths_since_last_major_derog', 
                  'mths_since_last_record', 'open_acc', 'pub_rec', 'revol_util']
# Store scalings in a dictionary so we can convert back later
scaled_features = {}
for each in quant_features:
    mean, std = X_all[each].mean(), X_all[each].std()
    scaled_features[each] = [mean, std]
    X_all.loc[:, each] = (X_all[each] - mean)/std

display(X_all.head())

from sklearn.model_selection import train_test_split

train_prop = 0.8

X_train, X_test, y_train, y_test = train_test_split(X_all, y_all, train_size=train_prop, random_state=1)

print("Training set has {} samples.".format(X_train.shape[0]))
print("Testing set has {} samples.".format(X_test.shape[0]))

def train_classifier(clf, X_train, y_train):
    ''' Fits a classifier to the training data. '''
    
    # Start the clock, train the classifier, then stop the clock
    start = time()
    clf.fit(X_train, y_train)
    end = time()
    
    # Print the results
    print("Trained model in {:.4f} seconds".format(end - start))

    
def predict_labels(clf, features, target):
    ''' Makes predictions using a fit classifier based on F1 score. '''
    
    # Start the clock, make predictions, then stop the clock
    start = time()
    y_pred = clf.predict(features)
    end = time()
    
    # Print and return results
    print("Made predictions in {:.4f} seconds.".format(end - start))
    return f1_score(target.values, y_pred, pos_label=1)


def train_predict(clf, X_train, y_train, X_test, y_test):
    ''' Train and predict using a classifer based on F1 score. '''
    
    # Indicate the classifier and the training set size
    print("Training a {} using a training set size of {}. . .".format(clf.__class__.__name__, len(X_train)))
    
    # Train the classifier
    train_classifier(clf, X_train, y_train)
    
    # Print the results of prediction for both training and testing
    print("F1 score for training set: {:.4f}.".format(predict_labels(clf, X_train, y_train)))
    print("F1 score for test set: {:.4f}.".format(predict_labels(clf, X_test, y_test)))


from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier(random_state=42, learning_rate=15)
train_classifier(clf, X_train, y_train)
predict_labels(clf, X_test, y_test)
train_predict(clf, X_train, y_train, X_test, y_test)


'''
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=42)
train_classifier(clf, X_train, y_train)
predict_labels(clf, X_test, y_test)
train_predict(clf, X_train, y_train, X_test, y_test)


# Import 'GridSearchCV' and 'make_scorer'
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer

# Create the parameters list you wish to tune
parameters = {'min_samples_split': [3, 5, 100, 1000]}

# Initialize the classifier
clf = RandomForestClassifier(random_state=42)

# Make an f1 scoring function using 'make_scorer' 
f1_scorer = make_scorer(f1_score, pos_label=1)

# Perform grid search on the classifier using the f1_scorer as the scoring method
grid_obj = GridSearchCV(estimator=clf, param_grid=parameters, scoring=f1_scorer, cv=10)

# Fit the grid search object to the training data and find the optimal parameters
grid_obj = grid_obj.fit(X_train, y_train)

# Get the estimator
clf = grid_obj.best_estimator_

# Report the final F1 score for training and testing after parameter tuning
print('')
print("Tuned model has a training F1 score of {:.4f}.".format(predict_labels(clf, X_train, y_train)))
print("Tuned model has a testing F1 score of {:.4f}.".format(predict_labels(clf, X_test, y_test)))
'''



'''
X_train_30000 = X_train[:30000]
y_train_30000 = y_train[:30000]
X_test_2000 = X_test[:2000]
y_test_2000 = y_test[:2000]


from sklearn.ensemble import RandomForestClassifier
clf2 = RandomForestClassifier(random_state=42)
train_classifier(clf2, X_train_30000, y_train_30000)
predict_labels(clf2, X_test_2000, y_test_2000)
train_predict(clf2, X_train_30000, y_train_30000, X_test_2000, y_test_2000)


from sklearn.svm import SVC
clf = SVC(random_state=42)
train_classifier(clf, X_train_30000, y_train_30000)
predict_labels(clf, X_test_2000, y_test_2000)
train_predict(clf, X_train_30000, y_train_30000, X_test_2000, y_test_2000)


# from sklearn import model_A
from sklearn.svm import SVC
# from sklearn import model_B
from sklearn.ensemble import AdaBoostClassifier
# from skearln import model_C
from sklearn.ensemble import RandomForestClassifier


# Initialize the three models
clf_A = SVC(random_state=42)
clf_B = AdaBoostClassifier(random_state=42)
clf_C = RandomForestClassifier(random_state=42)

clf_list = [clf_A, clf_B, clf_C]

# Execute the 'train_predict' function for each classifier
# train_predict(clf, X_train, y_train, X_test, y_test)
loop = [0, 1, 2]

for i in range(0, 3):
    clf = clf_list[i]
    print('')
    train_classifier(clf, X_train, y_train)
    predict_labels(clf, X_test, y_test)
    train_predict(clf, X_train, y_train, X_test, y_test)
    
'''