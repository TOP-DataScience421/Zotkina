y=int(input('введите год: '))
if (y % 4) == 0 and not (y % 100) == 0 or (y % 400) == 0:
    print('да')
else:
    print('нет')
    
#введите год: 2020
#да