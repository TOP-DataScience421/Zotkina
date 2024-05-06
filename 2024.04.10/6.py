num=int(input())
first3 = sum(int(d) for d in str(num)[:3])
second3 = sum(int(d) for d in str(num)[3:])
if first3 == second3:
    print('да')
else:
    print('нет')

#183534
#да    