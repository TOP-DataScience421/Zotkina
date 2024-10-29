import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal
from sklearn.ensemble import BaggingRegressor, RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from random import sample

def f(x):
    """Функция возвращает истинные и смещённые значения."""
    return x * np.sin(x), x * np.sin(x) + normal(size=x.shape)

def train_model(model_class, x_sample, y_sample, **params):
    x_train, x_test, y_train, y_test = train_test_split(
        x_sample, y_sample,
        test_size=0.3
    )
    model = model_class(**params)
    model.fit(x_train, y_train)
    return model, x_test, y_test

n = 100
x = np.linspace(-10, 10, n)
f_true, f_biased = f(x)

# количество итераций
N = 100

predictions_1 = []
for _ in range(N):
    # формирование подвыборки
    data_sample = sample(np.array([x, f_biased]).T.tolist(), int(n*0.4))
    x_sample, y_sample = np.array(data_sample).T
    x_sample = x_sample.reshape(-1, 1)
    y_sample = y_sample.reshape(-1, 1)
    # обучение подвыборки
    model, _, _ = train_model(
        DecisionTreeRegressor,
        x_sample,
        y_sample,
        max_depth=7
    )
    # предсказание моделью
    y_pred = model.predict(x.reshape(-1, 1))
    predictions_1.append(y_pred)

y_mean_1 = np.array(predictions_1).mean(axis=0)

# количество подвыборок
k = 10

predictions_2 = []
for _ in range(N):
    model, _, _ = train_model(
        BaggingRegressor,
        x.reshape(-1, 1),
        f_biased,
        estimator=DecisionTreeRegressor(max_depth=7),
        n_estimators=k,
        n_jobs=-1,
    )
    # уже усреднённое по k подвыборкам предсказание
    y_pred = model.predict(x.reshape(-1, 1))
    predictions_2.append(y_pred)

y_mean_2 = np.array(predictions_2).mean(axis=0)

# количество деревьев для RandomForestRegressor
n_estimators = 10

model_rfr = RandomForestRegressor(
    n_estimators=n_estimators,
    max_depth=7,
)

model_rfr.fit(x.reshape(-1, 1), f_biased)

y_pred_rfr = model_rfr.predict(x.reshape(-1, 1))

fig = plt.figure(layout='constrained')
axs = fig.subplots(1, 4)

axs[0].plot(x, f_true, lw=3)
axs[0].scatter(x, f_biased, s=30, c='#555')

axs[1].plot(x, f_true, lw=3)
for pred in predictions_1:
    axs[1].plot(x, pred, lw=0.1, c='#ba55d3')
axs[1].plot(x, y_mean_1, lw=2, c='#ffa500')

axs[2].plot(x, f_true, lw=3)
for pred in predictions_2:
    axs[2].plot(x, pred, lw=0.1, c='#ba55d3')
axs[2].plot(x, y_mean_2, lw=2, c='#ffa500')

axs[3].plot(x, f_true, lw=3)
axs[3].plot(x, y_pred_rfr, lw=2, c='#00ff00')

plt.show()