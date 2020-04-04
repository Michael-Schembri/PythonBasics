import csv 
import os
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()


countryDataFilename = os.path.realpath('.') + r'\ReadFromFiles\DataFiles\countryStats.csv'

#with open(countryDataFilename,'r') as myfile:
#    lines = csv.reader(myfile, delimiter = ',')
#    for line in lines:
#        print(line)
 
countryNames = []
countryPops = []
countryPerc = []

with open(countryDataFilename,'r') as myfile:
    lines = csv.DictReader(myfile, delimiter = ',')
    for line in lines:
        countryNames.append(line['CountryName'])
        countryPops.append(int(line['Population']))
        countryPerc.append(float(line['Percentage']))
        print(line)
 

y_pos = np.arange(len(countryNames))

plt.barh(y_pos, countryPops, color = 'green')
plt.yticks(y_pos, countryNames)

plt.xlabel('population')
plt.ylabel('country')

plt.title("European country populations")

plt.show()


