from pathlib import Path

def list_files(inp_path: str) -> 'tuple[str] | None':

#Функция принимает путь к каталогу в виде строки str, а далее выполняет поиск файлов в нужном каталоге. 
#На выходе - кортеж с именами найденных файлов или None, если нет такого каталога.

    path_to_parse = Path(inp_path)

    if not path_to_parse.is_dir(): 
        return None
    
#метод glob поможет найти все файлы в нужном каталоге
    files = [file.name for file in path_to_parse.glob('*') if file.is_file()]
    return tuple(files)
        
       
#>>> print(list_files('c:\\Git\\Zotkina\\2024.05.15\\data'))
#('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')
#>>> print(list_files('c:\\Git\\Zotkina\\2024.05.15\\datafunk'))
#None        
#>>> print(list_files('c:\\Git\\Zotkina\\2024.04.03'))
#('# HW 2024.04.03.txt', '1.py', '2.py', '3.py', '4.py', '5.py', '6.py')        
        


    

