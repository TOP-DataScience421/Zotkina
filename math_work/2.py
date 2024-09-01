import pandas as pd
import numpy as np

def read_and_process_csv(file_path):
    """Чтение данных и удаление строк с комментариями, разделение на столбцы"""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Удаление строк, начинающихся с '#'
    data_lines = [line for line in lines if not line.startswith('#')]
    
    # Преобразование данных в DataFrame
    data = pd.DataFrame([line.strip().split() for line in data_lines if len(line.strip().split()) == 2], columns=['Year', 'Value'])
    
    # Преобразование столбцов в нужные типы данных
    data['Year'] = pd.to_numeric(data['Year'], errors='coerce')
    data['Value'] = pd.to_numeric(data['Value'], errors='coerce')
    
    # Удаление строк с некорректными данными
    data = data.dropna()
    data['Year'] = data['Year'].astype(int)
    data['Value'] = data['Value'].astype(float)
    
    return data

def normalize(df):
    """Нормализация данных"""
    if df['Value'].std() == 0:
        raise ValueError("Стандартное отклонение равно нулю, нормализация невозможна.")
    df['Normalized'] = (df['Value'] - df['Value'].mean()) / df['Value'].std()
    return df[['Year', 'Normalized']]

def calculate_correlation(x, y):
    """Вычисление коэффициента корреляции"""
    if len(x) < 2 or len(y) < 2:
        return np.nan
    return np.corrcoef(x, y)[0, 1]

def find_max_correlation(df1, df2):
    """Поиск максимальной корреляции при различных временных сдвигах"""
    max_corr = -1
    best_shift = 0
    best_merged = None
    
    for shift in range(len(df2) + 1):
        shifted_df2 = df2.copy()
        shifted_df2['Year'] += shift
        merged_df = pd.merge(df1, shifted_df2, on='Year', how='inner', suffixes=('_1', '_2'))
        if len(merged_df) < 2:
            continue
        try:
            corr = calculate_correlation(merged_df['Normalized_1'], merged_df['Normalized_2'])
            if not np.isnan(corr) and corr > max_corr:
                max_corr = corr
                best_shift = shift
                best_merged = merged_df
        except ValueError as e:
            print(f"Ошибка: {e}")

    return max_corr, best_shift, best_merged

# Загрузка и обработка данных
df_malignancy = read_and_process_csv('early_malignancy.csv')
df_investments = read_and_process_csv('science_investetions.csv')

# Нормализация данных
df_malignancy_norm = normalize(df_malignancy)
df_investments_norm = normalize(df_investments)

# Поиск максимальной корреляции
max_corr, best_shift, best_merged = find_max_correlation(df_malignancy_norm, df_investments_norm)

# Вывод результатов
print(f'Максимальный коэффициент корреляции: {max_corr}')
print(f'Наилучший сдвиг: {best_shift} лет')

# Проверка для различных смещений
for shift in range(len(df_investments_norm) + 1):
    shifted_df_investments = df_investments_norm.copy()
    shifted_df_investments['Year'] += shift
    merged_df = pd.merge(df_malignancy_norm, shifted_df_investments, on='Year', how='inner', suffixes=('_malignancy', '_investments'))
    
    if len(merged_df) < 2:
        continue
    
    try:
        corr = calculate_correlation(merged_df['Normalized_malignancy'], merged_df['Normalized_investments'])
        print(f'Сдвиг: {shift} лет')
        print(f'Вариационные ряды: {list(merged_df["Normalized_malignancy"])} | {list(merged_df["Normalized_investments"])}')
        print(f'Коэффициент корреляции: {corr}')
        print()
    except ValueError as e:
        print(f"Ошибка: {e}")
