from matplotlib import (
    colormaps as cmap,
    pyplot as plt,
)
from pandas import (
    DataFrame, 
    read_csv,
)
import numpy as np
from datetime import timedelta as td
from pathlib import Path
from sys import path

data = read_csv(
    Path(path[0]) / 'births.csv',
    index_col='date',
    parse_dates=True,
)
data_acf = DataFrame()
data_acf['source'] = data
data_acf['-> 2 months'] = data.shift(2) 
data_acf['-> 6 months'] = data.shift(6) 
data_acf['-> 12 months'] = data.shift(12)

data_acf = data_acf.corr()['source']
data_acf.index = ['0', '2', '6', '12']

fig = plt.figure()
axs = fig.subplots(2, 1)

colors = cmap['twilight'](range(0, 256, 64))
axs[0].plot(data, c=colors[0])
axs[0].plot(data.shift(2), c=colors[1])
axs[0].plot(data.shift(6), c=colors[2])
axs[0].plot(data.shift(12), c=colors[3])

axs[1].scatter(data_acf.index, data_acf, s=100)
plt.show()