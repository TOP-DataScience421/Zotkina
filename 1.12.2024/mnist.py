from keras.layers import Dense, Input
from keras.losses import CategoricalCrossentropy
from keras.metrics import CategoricalAccuracy
from keras.models import Sequential
from keras.optimizers import Adam
from keras.utils import to_categorical

from numpy import load as np_load

from pathlib import Path
from sys import path


digits_imgs = np_load(Path(path[0]) / 'mnist.npz')

x_train = digits_imgs['x_train']
y_train = digits_imgs['y_train']
x_test = digits_imgs['x_test']
y_test = digits_imgs['y_test']

# >>> x_train.shape
# (60000, 28, 28)
# >>>
# >>> y_train.shape
# (60000,)
# >>>
# >>> x_test.shape
# (10000, 28, 28)
# >>>
# >>> y_test.shape
# (10000,)

# print(y_train[2])
# plt.imshow(x_train[2], cmap='gray')
# plt.show()


# понижение ранга тензора без потери данных
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

# масштабирование данных
x_train = x_train / 255
x_test = x_test / 255

# one hot encoding
#   0 -> [1 0 0 0 0 0 0 0 0 0]
#   1 -> [0 1 0 0 0 0 0 0 0 0]
#   2 -> [0 0 1 0 0 0 0 0 0 0]
#   3 -> [0 0 0 1 0 0 0 0 0 0]
#   4 -> [0 0 0 0 1 0 0 0 0 0]
#   5 -> [0 0 0 0 0 1 0 0 0 0]
#   6 -> [0 0 0 0 0 0 1 0 0 0]
#   7 -> [0 0 0 0 0 0 0 1 0 0]
#   8 -> [0 0 0 0 0 0 0 0 1 0]
#   9 -> [0 0 0 0 0 0 0 0 0 1]
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


# конструирование искусственной нейронной сети
model = Sequential(name='handwritten_digits_recognition')
model.add(Input(shape=(784,)))
model.add(Dense(units=400, activation='relu'))
model.add(Dense(units=200, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

# >>> model.summary()
# Model: "handwritten_digits_recognition"
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
# ┃ Layer (type)                         ┃ Output Shape                ┃         Param # ┃
# ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
# │ dense (Dense)                        │ (None, 400)                 │         314,000 │
# ├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
# │ dense_1 (Dense)                      │ (None, 200)                 │          80,200 │
# ├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
# │ dense_2 (Dense)                      │ (None, 10)                  │           2,010 │
# └──────────────────────────────────────┴─────────────────────────────┴─────────────────┘
#  Total params: 396,210 (1.51 MB)
#  Trainable params: 396,210 (1.51 MB)
#  Non-trainable params: 0 (0.00 B)

# конфигурирование искусственной нейронной сети
model.compile(
    loss=CategoricalCrossentropy(),
    optimizer=Adam(),
    metrics=[
        CategoricalAccuracy(name='accuracy'),
    ],
)


epochs = 15

print('\n ОБУЧЕНИЕ \n')
# обучение (предварительное) искусственной нейронной сети
training_results = model.fit(
    x_train,
    y_train,
    batch_size=128,
    epochs=epochs,
    validation_split=0.1,
    verbose=2,
)

print('\n ТЕСТИРОВАНИЕ \n')
# оценка эффективности обучения
scores = model.evaluate(
    x_test,
    y_test,
    batch_size=128,
    verbose=2,
    return_dict=True,
)

# fig = plt.figure(figsize=(12, 5))
# axs = fig.subplots(1, 2)

# axs[0].plot(training_results.history['loss'], label='loss')
# axs[0].plot(training_results.history['val_loss'], label='val_loss')
# axs[0].scatter(epochs, scores['loss'], s=50, c='r', label='test_loss')
# axs[0].legend()

# axs[1].plot(training_results.history['accuracy'], label='accuracy')
# axs[1].plot(training_results.history['val_accuracy'], label='val_accuracy')
# axs[1].scatter(epochs, scores['accuracy'], s=50, c='r', label='test_accuracy')
# axs[1].legend()

# plt.show()


from numpy import array
from PIL import Image


dir_path = Path(path[0]) / 'test/28'
images = [
    Image.open(img_path)
    for img_path in dir_path.iterdir()
]

digits_imgs_2 = [[[0]*28 for _ in range(28)] for _ in range(len(images))]

for i in range(len(images)):
    for y in range(28):
        for x in range(28):
            r, g, b, _ = images[i].load()[x,y]
            lum = (r + g + b) / 3
            digits_imgs_2[i][y][x] = round(lum)

digits_imgs_2 = array(digits_imgs_2)

x_test_2 = digits_imgs_2.reshape(len(images), 784)
x_test_2 = x_test_2 / 255

y_test_2 = array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 4, 8])
y_test_2 = to_categorical(y_test_2, 10)


print('\n РАСПОЗНАВАНИЕ \n')
results = model.predict(
    x_test_2, 
    verbose=2
)
# >>> results.round(2)
# array([[0.07, 0.  , 0.02, 0.  , 0.  , 0.  , 0.32, 0.  , 0.59, 0.  ],
#        [1.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ],
#        [1.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ],
#        [1.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ],
#        [0.  , 0.66, 0.  , 0.  , 0.  , 0.01, 0.32, 0.  , 0.01, 0.  ],
#        [0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 1.  , 0.  ],
#        [0.  , 1.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ],
#        [0.  , 0.99, 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ],
#        [0.  , 0.02, 0.09, 0.01, 0.  , 0.01, 0.  , 0.52, 0.34, 0.01],
#        [0.  , 0.  , 1.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ],
#        [0.  , 0.  , 0.01, 0.  , 0.  , 0.  , 0.  , 0.  , 0.99, 0.  ],
#        [0.  , 0.  , 0.  , 0.  , 1.  , 0.  , 0.  , 0.  , 0.  , 0.  ],
#        [0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 1.  , 0.  ]],
#       dtype=float32)

scores_2 = model.evaluate(
    x_test_2,
    y_test_2,
    verbose=2,
    return_dict=True,
)

print(
    '\nЗначение функции потерь: {loss:.3}\n'
    'Доля корректных распознаваний: {accuracy:.1%}'
    .format(**scores_2)
)

# Значение функции потерь: 2.04
# Доля корректных распознаваний: 69.2%

import tkinter as tk
from tkinter import messagebox
import numpy as np
from PIL import Image, ImageDraw

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Digit Recognizer")
        
        # Создание холста для рисования
        self.canvas = tk.Canvas(master, width=280, height=280, bg='white')
        self.canvas.pack()
        
        # Переменные для рисования
        self.last_x, self.last_y = None, None
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # Кнопка для предсказания
        self.predict_button = tk.Button(master, text="Predict Digit", command=self.predict_digit)
        self.predict_button.pack()

        # Хранение изображения
        self.image = Image.new("L", (280, 280), 255)  # Создаем белое изображение
        self.draw = ImageDraw.Draw(self.image)

    def paint(self, event):
        x, y = event.x, event.y
        if self.last_x and self.last_y:
            self.canvas.create_line((self.last_x, self.last_y, x, y), fill='black', width=15)
            self.draw.line((self.last_x, self.last_y, x, y), fill=0, width=15)
        self.last_x, self.last_y = x, y

    def reset(self, event):
        self.last_x, self.last_y = None, None

    def predict_digit(self):
        # Преобразование изображения в массив
        img_resized = self.image.resize((28, 28))
        img_array = np.array(img_resized)
        img_array = img_array.reshape(1, 784) / 255.0  # Нормализация

        # Предсказание
        predictions = model.predict(img_array)
        predicted_digit = np.argmax(predictions)

        # Отображение результата
        messagebox.showinfo("Prediction", f"Predicted Digit: {predicted_digit}")

# Создание основного окна
root = tk.Tk()
app = App(root)
root.mainloop()
