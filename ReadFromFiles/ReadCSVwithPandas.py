import csv 
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

countryDataFilename = os.path.realpath('.') + r'\ReadFromFiles\DataFiles\countryStats.csv'

df = pd.read_csv(countryDataFilename) 
 
fig = plt.figure()

y_pos = np.arange(len(df.index))

countryPops = df["Population"]
countryNames = df["CountryName"]

plt.barh(y_pos, countryPops, color = 'green')
plt.yticks(y_pos, countryNames)

plt.xlabel('population')
plt.ylabel('country')

plt.title("European country populations")

plt.show()


