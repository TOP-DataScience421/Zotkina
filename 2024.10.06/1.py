from matplotlib import pyplot as plt
from pandas import (
    concat,
    DataFrame,
    read_csv,
)
import pandas as pd
import numpy as np
from datetime import timedelta as td
from pathlib import Path
from sys import path

def predict_time_series(data, alpha):
    
    data_copy = data.copy()
    
    # Добавляем новую колонку для прогнозируемых значений
    data_copy['predicted'] = [float('nan')] * len(data_copy)
    
    
    data_copy.iloc[1, 1] = data_copy.iloc[0, 0]
    
    # подсчитываем прознозируемые значения 
    for t in range(2, len(data_copy)):
        predicted = alpha * data_copy.iloc[t-1, 0] + (1 - alpha) * data_copy.iloc[t-1, 1]
        data_copy.iloc[t, 1] = predicted
    
    # строим график
    fig = plt.figure()
    axs = fig.subplots()
    axs.plot(data_copy.iloc[:, 0])
    axs.plot(data_copy.iloc[:, 1], color='orange')
    plt.show()

# подготовка файла
file_path = 'crime.csv'
data = pd.read_csv(
    file_path,
    index_col='month',
    parse_dates=True,
    encoding='utf-8',
    sep=',',
    dtype={'Total_crimes': float}
)
alphas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

for alpha in alphas:
    predict_time_series(data, alpha)
