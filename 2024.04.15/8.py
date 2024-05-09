stroka = input('Введите имена файлов, разделённые точкой с запятой или пробелом: ')
names = stroka.split('; ')
score = {}
new_names = []
for name in names:
    if name not in score:
        score[name] = 1
        new_names.append(name)
    else:
        score[name] += 1
        name_not_extention, extention = name.rsplit('.', 1)
        new_name = f"{name_not_extention}_{score[name]}.{extention}"
        new_names.append(new_name)
new_names.sort()
for name in new_names:
    print(name)

#Введите имена файлов, разделённые точкой с запятой или пробелом: 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz
#1.py
#1_2.py
#1_3.py
#aux.h
#functions.h
#main.cpp
#main_2.cpp
#main_3.cpp
#src.tar.gz
#src.tar_2.gz

