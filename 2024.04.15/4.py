print('введите код: название ошибки:')
dict = {}

while True:
    data = input()
    if data == '':
        break
    key_value = data.split(maxsplit=2)
    key = key_value[0]
    value = key_value[1]
    dict[value]=key
    
search_value = input().strip()
if search_value in dict:
    print(dict[search_value])
else:
    print('! value error !')
    
#    1004 ER_CANT_CREATE_FILE
#    1005 ER_CANT_CREATE_TABLE
#    1006 ER_CANT_CREATE_DB
#    1007 ER_DB_CREATE_EXISTS
#    1008 ER_DB_DROP_EXISTS
#    1010 ER_DB_DROP_RMDIR
#    1016 ER_CANT_OPEN_FILE
#    1022 ER_DUP_KEY

#ER_DB_DROP_EXISTS
#1008

#введите код: название ошибки:
#4107 ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
#4108 ER_GIPK_COLUMN_EXISTS
#4111 ER_DROP_PK_COLUMN_TO_DROP_GIPK
#4113 ER_DA_EXPIRE_LOGS_DAYS_IGNORED
#4114 ER_CTE_RECURSIVE_NOT_UNION

#ER_CANT_OPEN_FILE
#! value error !
   