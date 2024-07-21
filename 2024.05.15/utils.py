from shutil import get_terminal_size

def important_message(*, message):
    # Получение ширины терминала и корректировка под полосу прокрутки
    width = get_terminal_size().columns - 1
    # Создание верхней и нижней границы рамки
    border = '#' + '=' * (width - 2) + '#'
    # Вычисление ширины внутреннего пространства рамки
    inner_width = width - 4  # Два пробела с каждой стороны
    # Центрирование сообщения внутри рамки
    padded_message = message.center(inner_width)
    # Сборка рамки и сообщения в одну строку
    framed_message = f"{border}\n#{' ' * (inner_width + 2)}#\n#  {padded_message}#\n#{' ' * (inner_width + 2)}#\n{border}"
    return framed_message
    

from shutil import copy2
from pathlib import Path

def load_file(*, file_path: Path):
    # Определение основного каталога (каталог задания)
    destination = Path(__file__).parent
    # Копирование файла
    new_path = copy2(file_path, destination)
    return new_path

import os
from pathlib import Path
from typing import List, Dict

def search_context(keyword: str, *additional_keywords: str, context: int = 0) -> List[Dict]:
    results = []
    data_directory = Path('data')
    txt_files = list(data_directory.glob('*.txt'))

    for txt_file in txt_files:
        with open(txt_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if any(keyword.lower() in word.lower() for word in line.split()):
                result = {
                    'keyword': keyword,
                    'filename': txt_file.name,
                    'line': i + 1,
                    'context': context,
                    'text': ''.join(lines[max(i-context, 0):min(i+context+1, len(lines))])
                }
                results.append(result)

            for additional_keyword in additional_keywords:
                if any(additional_keyword.lower() in word.lower() for word in line.split()):
                    result = {
                        'keyword': additional_keyword,
                        'filename': txt_file.name,
                        'line': i + 1,
                        'context': context,
                        'text': ''.join(lines[max(i-context, 0):min(i+context+1, len(lines))])
                    }
                    results.append(result)

    return results

def important_message(message):
    
    print("=" * 50)
    print(message)
    print("=" * 50)



