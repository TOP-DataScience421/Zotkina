from matplotlib import (
    colormaps as cmap,
    pyplot as plt,
)
from pandas import (
    DataFrame, 
    read_csv,
)
from statsmodels.graphics.tsaplots import plot_acf
from datetime import timedelta as td
from pathlib import Path
from sys import path

data = read_csv(
    Path(path[0]) / 'births.csv',
    index_col='date',
    parse_dates=True,
)
data_acf = DataFrame()
for i in range(0,20):
    data_acf[i] = data.shift(i)
data_acf = data_acf.corr()[0]


fig = plt.figure()
axs = fig.subplots(2,1)

axs[0].scatter(range(0, 20), data_acf, s=60)
plot_acf(data, axs[1], 20)
plt.show()