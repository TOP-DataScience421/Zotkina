n1 = int(input('введите первое число: '))
n2 = int(input('введите второе число: '))

if n1 % n2 == 0:
    print(f'{n1} делится на {n2} нацело \nчастное: {n1//n2}')
else:
    print(f'{n1} не делится на {n2} нацело \nнеполное частное: {n1//n2}\nостаток: {n1%n2}')
    
    
#введите первое число: 8
#введите второе число: 2
#8 делится на 2 нацело
#частное: 4

#введите первое число: 10
#введите второе число: 3
#10 не делится на 3 нацело
#неполное частное: 3
#остаток: 1