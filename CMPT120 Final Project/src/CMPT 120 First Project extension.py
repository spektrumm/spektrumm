# CMPT 120 Final Project - Machine Learning Part 3 - First Project Extension
# Author = Nathan Hare
# Date = Nov.22nd, 2020 (Started)
# Date = Nov. 26th, 2020 (Completed)
# Data File in question = forestfires.csv

# import the required modules
import sklearn
from sklearn.linear_model import LinearRegression
import turtle

# ---- STEP 1 ---- # 
# Process The Data

# ---- OUTPUT DATA ---- #
with open('forestfires.csv', 'r') as firesDataFileOutput:
    firesDataFileOutput.readline() # remove the header line from the file

    outputfireData = [] # create an empty list to append the output data to
    linesOutputfireData = firesDataFileOutput.readlines()

    # Split lines into sublists per each line based on a comma separator
    for lines in linesOutputfireData:
        linesOutputSplit = lines.split(',')
        outputfireData.append(linesOutputSplit[12])

    # create 2 lists to split our output data into
    trainOutputData = outputfireData[:int(len(outputfireData)*0.8)]
    testOutputData = outputfireData[-int(len(outputfireData)*0.2):]

    # convert the separated lists to type: float
    trainOutputFloat = [float(o) for o in trainOutputData]
    testOutputFloat = [float(o) for o in testOutputData]

# ---- INPUT DATA ---- #
with open('forestfires.csv', 'r') as firesDataFileInput:
    firesDataFileInput.readline() # remove the header line from the file
    inputfireData = []
    linesInputFireData = firesDataFileInput.readlines()

    # Split lines into sublists per each line based on a comma separator
    for lines in linesInputFireData:
        linesInputSplit = lines.split(',')
        inputfireData.append(linesInputSplit[4:11])

    # create 2 lists to split our output data into
    trainInputData = inputfireData[:int(len(inputfireData)*0.8)]
    testInputData = inputfireData[-int(len(inputfireData)*0.2):]

    n = 0
    trainInputFloat = []
    for i in range(len(trainInputData)):
        # convert the sublist items into type: float, for each item in the list
        trainFloatTemp = [float(i) for i in trainInputData[n]]
        trainInputFloat.append(trainFloatTemp)

        n += 1
    
    n = 0
    testInputFloat = []
    for i in range(len(testInputData)):
        # convert the sublist items into type: float, for each item in the list
        testFloatTemp = [float(i) for i in testInputData[n]]
        testInputFloat.append(testFloatTemp)

        n += 1


# ---- STEP 2 ---- # 
# Training Your Model

# set up the sklearn linear regression predictor
predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=trainInputFloat, y=trainOutputFloat)


# ---- STEP 3 ---- # 
# Using Your Model for Prediction

# apply the sklearn linear regression predictor
predictResultTest = predictor.predict(X=testInputFloat)
predictCoeffTest = predictor.coef_

# convert the outputted array to a list
predictResultList = predictResultTest.tolist()


# ---- STEP 4 ---- # 
# Visualizing the Performance of your Model

# step through the test list, removing any zeros present
n = 0
noZeroTest = []
noZeroResultList = []
for o in range(len(testOutputFloat)):

    if testOutputFloat[n] != 0.0:
        noZeroTest.append(testOutputFloat[n])
        noZeroResultList.append(predictResultList[n])
        n += 1
    else:
        n += 1

# calculate percent error of the machine learning prediction
n = 0
percentErrorList = []
for value in range(len(noZeroTest)):
    
    calcError = ((abs(noZeroTest[n] - noZeroResultList[n])) / noZeroTest[n])
    percentErrorList.append((calcError)*100)

    n += 1

# define a set of variables ranging from 
# <10% to >10% for adding to later
LessThan10 = 0
_10to20 = 0
_20to30 = 0
_30to40 = 0
_40to50 = 0
_50to60 = 0
_60to70 = 0
_70to80 = 0
_80to90 = 0
_90to100 = 0
GreaterThan100 = 0

# define a dictionary for use with the previously set variables
errorDict = {'less10': 0,
            '10to20': 0,
            '20to30': 0,
            '30to40': 0,
            '40to50': 0,
            '50to60': 0,
            '60to70': 0,
            '70to80': 0,
            '80to90': 0,
            '90to100': 0,
            'greater100': 0
            }

# loop the values in the list through conditional statements
# to organize the data into graphable categories.
n = 0
for percError in range(len(percentErrorList)):

    if percentErrorList[n] <= 10.0:
        LessThan10 += 1
        errorDict.update({'less10': LessThan10})
    elif percentErrorList[n] > 10.0 and percentErrorList[n] <= 20.0:
        _10to20 += 1
        errorDict.update({'10to20': _10to20})
    elif percentErrorList[n] > 20.0 and percentErrorList[n] <= 30.0:
        _20to30 += 1
        errorDict.update({'20to30': _20to30})
    elif percentErrorList[n] > 30.0 and percentErrorList[n] <= 40.0:
        _30to40 += 1
        errorDict.update({'30to40': _30to40})
    elif percentErrorList[n] > 40.0 and percentErrorList[n] <= 50.0:
        _40to50 += 1
        errorDict.update({'40to50': _40to50})
    elif percentErrorList[n] > 50.0 and percentErrorList[n] <= 60.0:
        _50to60 += 1
        errorDict.update({'50to60': _50to60})
    elif percentErrorList[n] > 60.0 and percentErrorList[n] <= 70.0:
        _60to70 += 1
        errorDict.update({'60to70': _60to70})
    elif percentErrorList[n] > 70.0 and percentErrorList[n] <= 80.0:
        _70to80 += 1
        errorDict.update({'70to80': _70to80})
    elif percentErrorList[n] > 80.0 and percentErrorList[n] <= 90.0:
        _80to90 += 1
        errorDict.update({'80to90': _80to90})
    elif percentErrorList[n] > 90.0 and percentErrorList[n] <= 100.0:
        _90to100 += 1
        errorDict.update({'90to100': _90to100})
    else:
        GreaterThan100 += 1
        errorDict.update({'greater100': GreaterThan100})
    
    n += 1

# add the axis labels for the graph to a list for use later
graphXLabels = ['<10',
                '10-20',
                '20-30',
                '30-40',
                '40-50',
                '50-60',
                '60-70',
                '70-80',
                '80-90',
                '90-100',
                '>100'
                ]
graphYLabels = ['10',
                '20',
                '30',
                '40',
                '50'
                ]

# initiate the turtle to draw the graph
wn = turtle.Screen()
tGraph = turtle.Turtle()
style = ('Helvetica', 12, 'bold')
yAxisMainLabel = 'Amount of\nPredictions\nin Given Range'
graphTitle = 'Machine Learning Prediction Percent Errors'

# function to draw the graph boundaries
def graphBounds():
    tGraph.up()
    tGraph.right(90)
    tGraph.forward(150)
    tGraph.left(90)
    tGraph.down()
    tGraph.forward(250)
    for x in range(3):
        tGraph.left(90)
        tGraph.forward(500)
    tGraph.left(90)
    tGraph.forward(250)

# function for drawing bars, assuming tGraph is facing upwards
def drawBar(barLen):
    tGraph.color('red')
    tGraph.fillcolor('red')
    tGraph.begin_fill()
    tGraph.forward(barLen)
    tGraph.right(90)
    tGraph.forward(43)
    tGraph.right(90)
    tGraph.forward(barLen)
    tGraph.right(90)
    tGraph.forward(43)
    tGraph.end_fill()
    # leave the turtle facing right once function concludes
    tGraph.left(180)
    tGraph.up()
    tGraph.forward(43)
    tGraph.down()

def nextBar():
    # leave space for inbetween the bars so they do not overlap
    tGraph.forward(2)
    tGraph.left(90)

graphBounds()

# move the turtle to label the X axis
tGraph.up()
tGraph.right(90)
tGraph.forward(36)
tGraph.write('Percent Error (by 10%)', font = style, align = 'center')
tGraph.right(180)
tGraph.forward(20)
tGraph.left(90)
tGraph.forward(240)
tGraph.right(180)

n = 0
for xLabel in range(len(graphXLabels)):
    tGraph.write(graphXLabels[n])
    tGraph.forward(45)

    n += 1

# reposition the turtle to begin drawing bars in the graph
tGraph.right(180)
tGraph.forward(502)
tGraph.right(90)
tGraph.forward(16)
tGraph.left(90)
tGraph.right(90)
tGraph.down()

# loop through the dictionary of categorized % errors 
# to draw each of their respective bars in the graph
for category, percValue in errorDict.items():

    drawBar(percValue * 10)
    nextBar()

# move the turtle around the graph to label the y axis properly
tGraph.up()
tGraph.color('black')
tGraph.right(90)
tGraph.forward(2)
tGraph.left(180)
tGraph.forward(500)
tGraph.right(90)
tGraph.forward(250)
tGraph.left(90)
tGraph.forward(106)
tGraph.right(90)
tGraph.write(yAxisMainLabel, font = style, align = 'center')
tGraph.right(90)
tGraph.forward(82)
tGraph.right(90)
tGraph.forward(250)
tGraph.write('0')
tGraph.right(180)

# iterate through the list and writing the values 
# to the graph at their respective points
n = 0
for yLabel in range(len(graphYLabels)):
    
    tGraph.forward(100)
    tGraph.write(graphYLabels[n])

    n += 1

tGraph.forward(16)
tGraph.right(90)
tGraph.forward(272)
tGraph.write(graphTitle, font = style, align = 'center')
tGraph.right(90)
tGraph.forward(16)
tGraph.left(90)

avgPredict = (sum(noZeroResultList)) / len(noZeroResultList)
avgActualValue = (sum(noZeroTest)) / len(noZeroTest)

# display a series of log messages that include exact numbers
# of the data used as well as the data displayed
print(f'log: filtered predictions list (no zeros)\n{len(noZeroResultList)}')
print(f'log: filtered actual value list (no zeros)\n{len(noZeroTest)}')
print(f'log: average of predict list:\n{avgPredict}')
print(f'log: average of actual value list:\n{avgActualValue}')
print(f'log: dictionary of % error categories\n{errorDict.items()}')

# keep the turtle window up until it is clicked
wn.exitonclick()