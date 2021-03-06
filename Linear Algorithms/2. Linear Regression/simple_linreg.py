# -*- coding: utf-8 -*-
"""Simple LinReg.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/133iuQbam8rrSew2vCuvQt-oaNq8NdUKl
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Calculate Mean From Dataset()
def mean(val):
  return np.sum(val,axis = 0) / float((len(val)))

def variance(val,mean):
  return np.sum([ (x - mean)**2 for x in val ])

def covariance(val1,val2): # describe if x and y variable relationship
  meanVal1 = mean(val1)
  meanVal2 = mean(val2)

  assert(len(val1) == len(val2),"GA SAMA SIZENYA BLOK")
  Covar = 0.0
  for i in range(0,len(val1)):
    Covar = Covar + ((val1[i] - meanVal1) * (val2[i] - meanVal2))
  
  return Covar

def Coefficients(dataset):
  x = [row[0] for row in dataset]
  y = [row[1] for row in dataset]
  mean_x , mean_y = mean(x) , mean(y)
  B1 = covariance(x,y) / variance(x,mean_x)
  B0 = mean_y - (B1 * mean(x))
  return [B0,B1]

def predictions(dataset,y_test):
  predict =[]
  b0,b1 = Coefficients(dataset)
  for x_test in y_tests:
    y_hat = b0 + b1 * x_test
    predict.append(y_hat)
  
  return predict


dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
x = [row[0] for row in dataset]
y = [row[1] for row in dataset]

print(f"Coefficients: b0 : {B0} , b1 : {B1})")
x_tests = [2,3,4,5,6]
x_test_true = [4,2,1,2,2]
ya = predictions(dataset,x_tests)
plt.scatter(x,y)
plt.scatter(x_tests,x_test_true)
plt.scatter(x_tests,ya)
plt.legend(["dataset","x_testTrue","Predicted"])
plt.show()