def math_function_resolver(math_func, *args, res_to_str=False):
    """
    Вычисляет округлённые значения для заданной математической функции.

    :param math_func: Математическая функция, которая принимает один аргумент x.
    :param args: Произвольное количество значений x для математической функции.
    :param res_to_str: Переключатель типа вычисляемых значений (bool), по умолчанию False.
    :return: Список округлённых значений функции, в формате int или str.
    """
    # Вычисление значений функции и округление
    results = [round(math_func(x)) for x in args]

    # Возвращение результатов в зависимости от переключателя
    return [str(result) for result in results] if res_to_str else results

# Примеры ручного тестирования
#>>> math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10))
#[2, 3, 4, 4, 4, 5, 6, 6, 6]
#>>> math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10))
#[2, 1, 0, 0, 0, -1, -2, -2, -2]
#>>> math_function_resolver(lambda x: 2.72**x, *range(1, 10), res_to_str=True)
#['3', '7', '20', '55', '149', '405', '1101', '2996', '8149']

