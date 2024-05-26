def numbers_strip(numbers: list[float], n: int =1, return_copy: bool = False) -> list[float]:
    # eсли нужно вернуть копию
    if return_copy:
        numbers = numbers.copy()
    
    # проверяем, что n не больше размера списка
    if n > len(numbers):
        raise ValueError("n cannot be greater than the size of the list")
    
    # удаляем n минимальных и n максимальных элементов
    for _ in range(n):
        numbers.remove(min(numbers))
        numbers.remove(max(numbers))
    
    return numbers
    
#ручное тестирование   
#sample = [10, 20, 30, 40, 50]
#>>> sample_stripped = numbers_strip(sample, 2, copy=True)
#Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
#TypeError: numbers_strip() got an unexpected keyword argument 'copy'
#>>> sample = [1, 2, 3, 4]
#>>> sample_stripped = numbers_strip(sample)
#>>> sample_stripped
#[2, 3]
#>>> sample is sample_stripped
#True
#>>>    