fruits=input()
f_list=[]
while fruits != '':
    f_list.append(fruits)
    fruits=input()
for f in f_list:
        if len(f_list) == 1:
            print(f_list[0])
        elif len(f_list) == 2:
            print(' и '.join(f_list))
        else:
            print(', '.join(f_list[:-1]) + ' и ' + f_list[-1])


#яблоко

#яблоко

#яблоко
#груша

#яблоко и груша
#яблоко и груша

#яблоко
#груша
#слива
#апельсин

#яблоко, груша, слива и апельсин
#яблоко, груша, слива и апельсин
#яблоко, груша, слива и апельсин
#яблоко, груша, слива и апельсин            