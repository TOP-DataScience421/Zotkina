import numpy as np
import matplotlib.pyplot as plt

def step(x, cutoff=0):
    return 1 if x > cutoff else 0

def linear(x, k=1, b=0):
    return k * x + b

def relu(x, k=1, cutoff=0):
    return k * x if x > cutoff else 0

def lrelu(x, k1=1, k2=0.1, cutoff=0):
    return k1 * x if x > cutoff else k2 * x

def prelu(x, k=1, left=-1, right=1, normalization=True):
    if x <= left:
        return 0
    elif right <= x:
        return 1 if normalization else right
    else:
        return (k * x - left) / (k * right) if normalization else k * x - left

def sigmoid(x, a=1, b=0):
    return 1 / (1 + np.exp(-a * x + b))

def tanh(x, a=1, b=0):
    return np.tanh(a * x + b)

# Нормализация данных
def normalize(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

# Генерация данных
np.random.seed(42)
data_uniform = np.random.uniform(-10, 10, 1000)
data_normal = np.random.normal(0, 1, 1000)
data_linear = np.linspace(-10, 10, 1000)

# Нормализация данных
data_uniform_normalized = normalize(data_uniform)
data_normal_normalized = normalize(data_normal)
data_linear_normalized = normalize(data_linear)

# Применение функций активации
def apply_activations(data):
    return {
        'step': np.array([step(x) for x in data]),
        'linear': np.array([linear(x) for x in data]),
        'relu': np.array([relu(x) for x in data]),
        'lrelu': np.array([lrelu(x) for x in data]),
        'prelu': np.array([prelu(x) for x in data]),
        'sigmoid': np.array([sigmoid(x) for x in data]),
        'tanh': np.array([tanh(x) for x in data]),
    }

# Применение функций активации
results_uniform = apply_activations(data_uniform)
results_normal = apply_activations(data_normal)
results_linear = apply_activations(data_linear)

results_uniform_normalized = apply_activations(data_uniform_normalized)
results_normal_normalized = apply_activations(data_normal_normalized)
results_linear_normalized = apply_activations(data_linear_normalized)

# Визуализация результатов
fig, axs = plt.subplots(6, 2, figsize=(12, 18), constrained_layout=True)

# Визуализация ненормализованных данных
for i, (title, result) in enumerate(results_uniform.items()):
    if i < len(axs):  # Убедитесь, что индекс не выходит за пределы
        axs[i][0].plot(data_uniform, result)
        axs[i][0].set_title(f'{title} (Uniform)')

for i, (title, result) in enumerate(results_normal.items()):
    if i < len(axs):  # Убедитесь, что индекс не выходит за пределы
        axs[i][1].plot(data_normal, result)
        axs[i][1].set_title(f'{title} (Normal)')

plt.show()

# Визуализация результатов для нормализованных данных
fig, axs = plt.subplots(6, 2, figsize=(12, 18), constrained_layout=True)

for i, (title, result) in enumerate(results_uniform_normalized.items()):
    if i < len(axs):  # Убедитесь, что индекс не выходит за пределы
        axs[i][0].plot(data_uniform_normalized, result)
        axs[i][0].set_title(f'{title} (Uniform Normalized)')

for i, (title, result) in enumerate(results_normal_normalized.items()):
    if i < len(axs):  # Убедитесь, что индекс не выходит за пределы
        axs[i][1].plot(data_normal_normalized, result)
        axs[i][1].set_title(f'{title} (Normal Normalized)')

plt.show()
