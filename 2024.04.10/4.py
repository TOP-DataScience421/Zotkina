n = abs(int(input()))
y = int('9'*n)
x = int('9'*(n-1))
lower_value = x 
upper_value = y
simple_num = 0
for number in range(lower_value, upper_value): 
    if number > 1: 
        for i in range(2, number): 
            if(number % i) == 0:
                break 
        else:
            simple_num += 1
            
print(simple_num)

#3
#143

#4
#1061