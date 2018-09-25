#https://www.hackerrank.com/challenges/predicting-office-space-price/problem

#The first line contains two space separated integers, F and N.
#  Over here, F is the number of observed features.
#  N is the number of rows for which features as well as price per square-foot have been noted. 
#This is followed by a table having F+1 columns and
#  N rows with each row in a new line and each column separated by a single space. 
# The last column is the price per square foot.

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Perceptron, LinearRegression
from sklearn import linear_model
from  matplotlib import pyplot as plt
import numpy as np

F_count, N = input().split()
F_count = int(F_count)
N = int(N)
Feature_list = []
Price_list = []
for i in range(N):
    row = input().split()
    row = [float(row[i]) for i in range(len(row))]
    Feature_list.append(row[0:F_count])
    Price_list.append(row[-1])



#X = np.array(Feature_list)
#y = np.array(Price_list)

X = Feature_list
y = Price_list
# PolynomialFeatures (prepreprocessing)
poly = PolynomialFeatures(degree=2)
X_ = poly.fit_transform(X)
#X_test = np.array([[0.05, 0.54], [0.91, 0.91], [0.31, 0.76], [0.51, 0.31]])
#X_test_ = poly.fit_transform(X_test)

# Instantiate
lg = LinearRegression()

# Fit
lg.fit(X_, y)

# Obtain coefficients
lg.coef_

# Predict
N = int(input())
X_test = []
for j in range(N):
    row = input().split()
    row = np.array([float(row[i]) for i in range(len(row))])
    X_test.append(row)
X_test = np.array(X_test)
if N == 1:
    X_test = X_test.reshape(1, -1)

X_test_ = poly.fit_transform(X_test)
for k in range(N):
    print(round(lg.predict(X_test_)[k], 2))