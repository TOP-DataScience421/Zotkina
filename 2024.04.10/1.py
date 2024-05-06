x=int(input())
a=[]
while x % 7==0:
    a.append(x)
    x=int(input())
a.reverse()
result=(filter(lambda x: type (x) is int, a))
print(*result, sep=' ')

#7
#7
#14
#21
#13
#21 14 7 7
