# CMPT 120 Final Project - Machine Learning Part 1 - Building Our First Machine Learning Model
# Author = Nathan Hare
# Date = Nov.22nd, 2020 (Started)
# Date = Nov.22nd, 2020 (Completed)

# import the required modules
import sklearn
from sklearn.linear_model import LinearRegression
import random
from random import randint

# ---- STEP 1 ---- #
# Figuring out algebraic relationship betwwen inputs and outputs

# coefficients = 1,2,3
# therefore, equation: y = 1*x1 + 2*x2 + 3*x3

# ---- STEP 2 ---- #
# Generating a training set

x1list = []
x2list = []
x3list = []

inputList = []
outputList = []

# generate the test data to train the machine learning model
for x in range(100):
    x1list.append(randint(0,1000))
    x2list.append(randint(0,1000))
    x3list.append(randint(0,1000))

# map the 3 individual lists to become 
# a list of 100 sublists, each of length 3
inputList = list(map(list, zip(x1list, x2list, x3list)))

# loop through 100 values, 
# applying the equation from Step 1
n = 0
for x in range(100):
    y = 1*(x1list[n]) + 2*(x2list[n]) + 3*(x3list[n])
    outputList.append(y)

    n += 1

# display some previously generated and 
# calculated values for future comparison/testing
print(f'Manual inputList: \n{inputList}')
print(f'Manual outputList: \n{outputList}')

# ---- STEP 3 ---- #
# Training the machine learning model

# set up the sklearn linear regression predictor
predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=inputList, y=outputList)

# ---- STEP 4 ---- #
# Using the model for prediction

# apply the sklearn linear regression predictor
predictResult = predictor.predict(X=inputList)
predictCoeff = predictor.coef_

# display the output predicted values for comparison with 
# the previously natively generated + calculated values.
print(f'Prediction: {predictResult}')
print(f'Coefficients: {predictCoeff}')