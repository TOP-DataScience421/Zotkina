import numpy as np
from scipy import stats

def print_result(title, observed, critical, result):
    print(f"\n{title}")
    print(f"  Наблюдаемое значение: {observed:.4f}")
    print(f"  Критическое значение: {critical:.4f}")
    print(f"  Вывод: {result}")

def print_variation_series(title, data):
    print(f"\n{title}")
    sorted_data = np.sort(data)
    print("  Вариационный ряд: ", end="")
    print(", ".join(f"{x}" for x in sorted_data))

def normality_test(data):
    # Проверка на нормальность с помощью теста Шапиро-Уилка
    stat, p_value = stats.shapiro(data)
    print("\nПроверка гипотезы о нормальном распределении")
    print(f"  Статистика теста: {stat:.4f}")
    print(f"  p-значение: {p_value:.4f}")
    if p_value > 0.05:
        print("  Вывод: Данные соответствуют нормальному распределению")
    else:
        print("  Вывод: Данные не соответствуют нормальному распределению")

def grubb_test(data, alpha=0.05):
    # Проверка крайних значений с помощью критерия Граббса
    data = np.sort(data)
    n = len(data)
    
    # Груббс тест для крайних значений
    G = max((data[-1] - np.mean(data)) / np.std(data, ddof=1), (np.mean(data) - data[0]) / np.std(data, ddof=1))
    critical_value = stats.t.ppf(1 - alpha / (2 * n), n - 2) * np.sqrt((n - 1) / (n - 2 + np.square(stats.t.ppf(1 - alpha / (2 * n), n - 2))))

    print("\nПроверка принадлежности крайних значений генеральным совокупностям")
    print(f"  Наблюдаемое значение: {G:.4f}")
    print(f"  Критическое значение: {critical_value:.4f}")
    if G > critical_value:
        print("  Вывод: Крайние члены не принадлежат генеральным совокупностям")
    else:
        print("  Вывод: Крайние члены принадлежат генеральным совокупностям")

def test_hypotheses(N, R):
    # Проверка нормальности распределения
    normality_test(N)
    normality_test(R)

    # Проверка крайних значений
    grubb_test(N)
    grubb_test(R)

    # Проверка равенства дисперсий с помощью F-теста
    var_N = np.var(N, ddof=1)
    var_R = np.var(R, ddof=1)
    f_stat = var_N / var_R
    df1 = len(N) - 1
    df2 = len(R) - 1
    f_critical = stats.f.ppf(0.95, df1, df2)
    
    print("\nПроверка гипотезы о равенстве дисперсий")
    print(f"  Наблюдаемое значение F: {f_stat:.4f}")
    print(f"  Критическое значение F: {f_critical:.4f}")
    if f_stat > f_critical:
        print("  Вывод: Дисперсии значимо различаются")
    else:
        print("  Вывод: Дисперсии не значимо различаются")

    # Проверка равенства средних значений с помощью t-теста
    t_stat, p_value = stats.ttest_ind(N, R, equal_var=True)
    
    print("\nПроверка гипотезы о равенстве средних значений")
    print(f"  Статистика t: {t_stat:.4f}")
    print(f"  p-значение: {p_value:.4f}")
    if p_value < 0.05:
        print("  Вывод: Средние значения значимо различаются")
    else:
        print("  Вывод: Средние значения не значимо различаются")

if __name__ == "__main__":
    # Данные
    N = np.array([1661, 1842, 2125, 2430, 2202, 3006, 2102, 1702, 2333, 1969])
    R = np.array([2695, 3053, 2754, 3430, 2871, 2983, 2836, 3082, 2881, 2969, 2886, 3202, 2943, 2961])
    
    # Номер варианта
    print("Вариант 3")
    
    # Вывод вариационных рядов
    print_variation_series("Вариационный ряд N", N)
    print_variation_series("Вариационный ряд R", R)
    
    # Проверка гипотез
    test_hypotheses(N, R)
