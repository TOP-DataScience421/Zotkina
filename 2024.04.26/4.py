def repeat(_func=None, *, num_times=2):

    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)
        
#пример ручного теста
#>>> @repeat(num_times=4)
#... def testing_function():
#...     print('python')
#...
#>>> testing_function()
#python
#python
#python
#python