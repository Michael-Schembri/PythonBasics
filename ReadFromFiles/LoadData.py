import csv 
import os

def loadData(fileName):
    outputLines = []
    if (os.path.exists(fileName)):
        with open(fileName,'r') as myfile:
            lines = csv.DictReader(myfile, delimiter = ',')
            for line in lines:
                outputLines.append(line)
    return outputLines