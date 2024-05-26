def taxi_cost(route_length: int, waiting_time: int =0) -> int | None:
    # проверяем на отрицательные
    if route_length <0 or waiting_time <0:
        return None
    
    # задаем базовую стоимость
    cost =80
    
    # считаем стоимость за длину маршрута
    if route_length >0:
        cost += (route_length //150) *6
    else:
        # отмена поездки
        cost +=80 + waiting_time *3
    
    # расчёт стоимости за время ожидания
    cost += waiting_time *3
    
    # округление стоимости до целого числа
    return round(cost)
    
#проверка
#>>> taxi_cost(1500)
#140
#>>> taxi_cost(2560)
#182
#>>> taxi_cost(0, 5)
#190
#>>> taxi_cost(42130, 8)
#1784
#>>> print(taxi_cost(-300))
#None
>>>