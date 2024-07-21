from utils import load_file
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
import os

def ask_for_file():
    while True:
        file_path = input("Введите путь к файлу: ")
        if not Path(file_path).is_file():
            print("! по указанному пути отсутствует необходимый файл !")
            continue
        break

    # Копирование файла и получение нового пути
    new_path = load_file(file_path=file_path)
    
    # Импорт модуля из нового местоположения
    spec = spec_from_file_location("config_module", new_path)
    config_module = module_from_spec(spec)
    spec.loader.exec_module(config_module)
    
    return config_module

if __name__ == "__main__":
    config_module = ask_for_file()
    print(config_module.defaults)

#Пример ручного теста
#Введите путь к файлу: c:\Git\Zotkina\2024.05.15\conf.py
#! по указанному пути отсутствует необходимый файл !
#Введите путь к файлу: c:\Git\Zotkina\2024.05.15\data\conf.py
#{'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}
