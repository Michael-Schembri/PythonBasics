import matplotlib.pyplot as plt
import numpy as np
import LoadData as reader
import os

fig = plt.figure()
countryDataFilename = os.path.realpath('.') + r'\ReadFromFiles\DataFiles\countryStats.csv'

data = reader.loadData(countryDataFilename)
 
countryNames = []
countryPops = []
countryPerc = []

print(dir(reader))

for line in data:
    countryNames.append(line['CountryName'])
    countryPops.append(int(line['Population']))
    countryPerc.append(float(line['Percentage']))
#    print(line)


y_pos = np.arange(len(countryNames))

plt.barh(y_pos, countryPops, color = 'green')
plt.yticks(y_pos, countryNames)

plt.xlabel('population')
plt.ylabel('country')

plt.title("European country populations")

plt.show()


