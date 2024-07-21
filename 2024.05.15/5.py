from datetime import datetime

def logger(func):
    def wrapper(*args, **kwargs):
        currenttime = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
        result = func(*args, **kwargs)
        with open('data/function_calls.log', 'a') as f:
            log_entry = f"{currenttime} - {func.__name__}{args}{kwargs} -> {result}\n"
            f.write(log_entry)
        return result

    return wrapper   
    
#python -i 5.py
#>>> def div_round(num1, num2, *, digits=0):
#...     return round(num1 / num2, digits)
#...
#>>> div_round = logger(div_round)
#>>> div_round(2, 3, digits=2)
#0.67    