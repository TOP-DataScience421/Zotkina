import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Функция правильного формата данных
def read_and_process_data(filepath):
    # Чтение данных из CSV файла
    df = pd.read_csv(filepath, header=None)
    
    # Проверка названия столбцов
    print("Столбцы в файле:", df.columns.tolist())
    
    # Присвоение правильных имен столбцам
    df.columns = ['date_value']
    
    # Разделение строки на два столбца: дата и значение
    df[['date', 'value']] = df['date_value'].str.split(' ', n=1, expand=True)
    
    # Замена кириллических месяцев на латинские
    month_replacements = {
        'янв': 'Jan',
        'фев': 'Feb',
        'мар': 'Mar',
        'апр': 'Apr',
        'май': 'May',
        'июн': 'Jun',
        'июл': 'Jul',
        'авг': 'Aug',
        'сен': 'Sep',
        'окт': 'Oct',
        'ноя': 'Nov',
        'дек': 'Dec'
    }
    
    for cyrillic, latin in month_replacements.items():
        df['date'] = df['date'].str.replace(cyrillic, latin, regex=False)
    
    # Преобразование даты в формат datetime
    df['date'] = pd.to_datetime(df['date'], format='%d.%b.%y', errors='coerce')
    
    # Преобразование значения в числовой формат
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    
    # Удаление временного столбца
    df = df[['date', 'value']]
    
    return df

# Чтение и обработка данных
urals_df = read_and_process_data('urals_oil_rus_export_prices.csv')
dizel_df = read_and_process_data('dizel_fuel_rus_prices.csv')

# Убедимся, что данные отсортированы по дате
urals_df = urals_df.sort_values(by='date')
dizel_df = dizel_df.sort_values(by='date')

# Функция для расчета коэффициента корреляции и построения регрессии
def calculate_correlation_and_regression(df1, df2, shift_months):
    shift_days = shift_months * 30
    shifted_df2 = df2.copy()
    shifted_df2['date'] = shifted_df2['date'] + pd.DateOffset(days=shift_days)
    
    # Объединение данных по дате
    merged_df = pd.merge(df1, shifted_df2, on='date', suffixes=('_df1', '_df2'))
    
    # Корреляция
    correlation = merged_df['value_df1'].corr(merged_df['value_df2'])
    
    # Построение регрессии
    X = merged_df['value_df1'].values
    y = merged_df['value_df2'].values
    A = np.vstack([X, np.ones(len(X))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    
    return correlation, m, c

# Сдвиг в месяцах
shift_months_range = range(-12, 13)  # от -12 до +12 месяцев

# Сохранение лучших результатов
best_correlation = -1
best_shift = 0
best_m = 0
best_c = 0

# Сохранение результатов
results = []

for shift in shift_months_range:
    correlation, m, c = calculate_correlation_and_regression(urals_df, dizel_df, shift)
    results.append((shift, correlation))
    if correlation > best_correlation:
        best_correlation = correlation
        best_shift = shift
        best_m = m
        best_c = c

# Печать результатов
print("Результаты корреляции для различных сдвигов:")
for shift, correlation in results:
    print(f"Сдвиг: {shift} мес, Корреляция: {correlation:.4f}")

print(f"\nНаилучший сдвиг: {best_shift} мес, Корреляция: {best_correlation:.4f}")
print(f"Уравнение регрессии: y = {best_m:.4f}x + {best_c:.4f}")

# Построение графика
shifted_df2_best = dizel_df.copy()
shifted_df2_best['date'] = shifted_df2_best['date'] + pd.DateOffset(months=best_shift)
merged_df_best = pd.merge(urals_df, shifted_df2_best, on='date', suffixes=('_df1', '_df2'))

plt.figure(figsize=(10, 6))
plt.scatter(merged_df_best['value_df1'], merged_df_best['value_df2'], color='blue', label='Данные')
plt.plot(merged_df_best['value_df1'], best_m * merged_df_best['value_df1'] + best_c, color='red', label='Регрессия')
plt.xlabel('Цены на нефть (Urals)')
plt.ylabel('Цены на дизель (Dizel)')
plt.title('Регрессия между ценами на нефть и дизель')
plt.legend()
plt.grid(True)

# Сохранение графика
plt.savefig('regression_plot.png', dpi=300)
plt.show()
