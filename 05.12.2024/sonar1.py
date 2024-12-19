from keras.models import Sequential
from keras.layers import Dense, Input, Dropout, BatchNormalization
from keras.losses import BinaryCrossentropy
from keras.metrics import BinaryAccuracy
from keras.optimizers import Adam

from matplotlib import pyplot as plt
from pandas import read_csv
from sklearn.model_selection import train_test_split

from pathlib import Path
from sys import path

# Загрузка данных
raw_data = read_csv(Path(path[0]) / 'sonar.csv', header=None)
raw_data[60] = raw_data[60].replace({'R': 0, 'M': 1})

# Разделение данных на обучающую и тестовую выборки
x_train, x_test, y_train, y_test = train_test_split(
    raw_data.iloc[:, :-1],
    raw_data.iloc[:, -1],
    test_size=0.2,
    random_state=1,
)

# Создание модели
model = Sequential(name='hydroacoustic_response_recognition')
model.add(Input((60,)))
model.add(Dropout(0.2))
model.add(Dense(60))
model.add(BatchNormalization())  # Добавление слоя пакетной нормализации
model.add(Dense(60, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(30))
model.add(BatchNormalization())  # Добавление слоя пакетной нормализации
model.add(Dense(30, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Компиляция модели
model.compile(
    loss=BinaryCrossentropy(),
    optimizer=Adam(learning_rate=0.001),
    metrics=[
        BinaryAccuracy(name='accuracy'),
    ],
)

# Обучение модели
epochs = 100
training_results = model.fit(
    x_train,
    y_train,
    batch_size=8,
    epochs=epochs,
    validation_split=0.2,
    verbose=0,
)

# Оценка модели
scores = model.evaluate(
    x_test,
    y_test,
    batch_size=8,
    verbose=0
)

# Визуализация результатов
fig = plt.figure(figsize=(12, 5))
axs = fig.subplots(1, 2)

axs[0].plot(training_results.history['loss'], label='loss')
axs[0].plot(training_results.history['val_loss'], label='val_loss')
axs[0].scatter(epochs, scores[0], s=50, c='r', label='test_loss')
axs[0].legend()

axs[1].plot(training_results.history['accuracy'], label='accuracy')
axs[1].plot(training_results.history['val_accuracy'], label='val_accuracy')
axs[1].scatter(epochs, scores[1], s=50, c='r', label='test_accuracy')
axs[1].legend()

plt.show()
