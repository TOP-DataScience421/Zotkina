from keras.layers import Conv2D, MaxPooling2D, Flatten
from keras.layers import Dense, Input
from keras.losses import CategoricalCrossentropy
from keras.metrics import CategoricalAccuracy
from keras.models import Sequential
from keras.optimizers import Adam
from keras.utils import to_categorical

from numpy import load as np_load
from matplotlib import pyplot as plt
from pathlib import Path
from sys import path

# Загрузка данных
digits_imgs = np_load(Path(path[0]) / 'mnist.npz')

x_train = digits_imgs['x_train']
y_train = digits_imgs['y_train']
x_test = digits_imgs['x_test']
y_test = digits_imgs['y_test']

# Преобразование данных
x_train = x_train.reshape(60000, 28, 28, 1)  # Добавление размерности для канала
x_test = x_test.reshape(10000, 28, 28, 1)

# Масштабирование данных
x_train = x_train / 255.0
x_test = x_test / 255.0

# One hot encoding
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Конструирование сверточной нейронной сети
model = Sequential(name='handwritten_digits_recognition')

# Первый суперслой: свертка и подвыборка
model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Второй суперслой: свертка и подвыборка
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Преобразование данных в вектор для полносвязного слоя
model.add(Flatten())

# Полносвязные слои
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

# Компиляция модели
model.compile(
    loss=CategoricalCrossentropy(),
    optimizer=Adam(),
    metrics=[
        CategoricalAccuracy(name='accuracy'),
    ],
)

# Обучение модели
epochs = 20
print('\n ОБУЧЕНИЕ \n')
training_results = model.fit(
    x_train,
    y_train,
    batch_size=128,
    epochs=epochs,
    validation_split=0.1,
    verbose=2,
)

# Оценка модели
print('\n ТЕСТИРОВАНИЕ \n')
scores = model.evaluate(
    x_test,
    y_test,
    batch_size=128,
    verbose=2,
    return_dict=True,
)

# Визуализация результатов
fig = plt.figure(figsize=(12, 5))
axs = fig.subplots(1, 2)

axs[0].plot(training_results.history['loss'], label='loss')
axs[0].plot(training_results.history['val_loss'], label='val_loss')
axs[0].scatter(epochs, scores['loss'], s=50, c='r', label='test_loss')
axs[0].legend()

axs[1].plot(training_results.history['accuracy'], label='accuracy')
axs[1].plot(training_results.history['val_accuracy'], label='val_accuracy')
axs[1].scatter(epochs, scores['accuracy'], s=50, c='r', label='test_accuracy')
axs[1].legend()

plt.show()
