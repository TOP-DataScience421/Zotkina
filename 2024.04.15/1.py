email=input('Введите электронный адрес: ')
#адрес почты должен содержать один символ собаки
#символ собака не должен быть первым
#символ точка должен хотя бы 1 раз встречаться
#точка должна стоять после собаки

if email.count('@') == 1 and email[0] != '@' and email.count('.') > 0 and email.rfind('@') < email.find('.'):
    print('да')
else:
    print('нет')

#Введите электронный адрес: zotkina@yandex.ru
#да

#Введите электронный адрес: zzz@dfgfd
#нет

#Введите электронный адрес: sgd@ya.ru
#да
