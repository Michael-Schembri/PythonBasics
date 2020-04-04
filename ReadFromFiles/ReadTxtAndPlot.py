import os
import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure() 

countryListFilename = os.path.realpath('.') + r'\ReadFromFiles\DataFiles\countryList.txt'
countryPopFilename = os.path.realpath('.') + r'\ReadFromFiles\DataFiles\CountryPops.txt'

with open(countryListFilename,'r') as reader:
    nameData = reader.readlines()

with open(countryPopFilename,'r') as reader:
    popDataStr = reader.readlines()
#convert string array to int array
popDataInt = [int(population) for population in popDataStr]

y_pos = np.arange(len(nameData))

formatText = "Population of country {0} is {1}"
plt.barh(y_pos, popDataInt, color = 'green')
plt.yticks(y_pos, nameData)

plt.xlabel('population')
plt.ylabel('country')


plt.title("European country populations")

plt.show()

