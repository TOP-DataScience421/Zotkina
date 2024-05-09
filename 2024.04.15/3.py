print('Введите элементы первого списка:')
first_list = list(map(int, input().split()))
print('Введите элементы второго списка:')
second_list = list(map(int, input().split()))

for i in range(0,len(first_list)):
        if first_list[i:i+len(second_list)] == second_list:
            print('Да')
            break
        else:
            print('Нет')
            break

#Введите элементы первого списка:
#1 2 3 4 5
#Введите элементы второго списка:
#1 2 3
#Да

#Введите элементы первого списка:
#1 2 3 4 5
#Введите элементы второго списка:
#2 4 6 8
#Нет            