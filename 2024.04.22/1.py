def strong_password(password: str) -> bool:
    # Проверка длины пароля
    if len(password) <8:
        return False
    
    # Проверка наличия в пароле буквенных символов в обоих регистрах
    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    if not (upper and lower):
        return False
    
    # Проверка наличия минимум двух символов цифр
    digits = sum(char.isdigit() for char in password)
    if digits <2:
        return False
    
    # Проверка наличия символов прочих категорий
    other = any(not char.isalnum() for char in password)
    if not other:
        return False
    
    # Если все условия выполнены, пароль надёжный
    return True

# Пример ручного тестирования:
#>>> strong_password('aP3:kD_l3')
#True
#>>> strong_password('password')
#False
#>>> strong_password('passwoFdf')
#False
