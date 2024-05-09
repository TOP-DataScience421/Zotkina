numbers = input('Введите строку: ')
symbols = {'0', '1'}

if numbers.startswith('0b'):
    numbers = numbers[2:]
elif numbers.startswith('b'):
    numbers = numbers[1:]
else: set(numbers).issubset(symbols)    

if set(numbers).issubset(symbols):
    print ('да')
else: 
    print ('нет')
    
#Введите строку: 0101
#да  

#Введите строку: 1b0101
#нет  