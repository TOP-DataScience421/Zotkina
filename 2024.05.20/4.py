import csv
from pathlib import Path
"""
Этот код определяет класс CountableNouns с необходимыми полями, методами и логикой:

Поле db_path указывает на путь к файлу с базой существительных.
Поле words хранит словарь с существительными и их формами.
Метод load_words загружает данные из CSV файла в словарь words.
Метод save_words добавляет новые существительные в словарь и записывает их в CSV файл.
Метод pick возвращает существительное, согласованное с переданным числом. Если слово отсутствует в базе, вызывается метод save_words.
"""
class CountableNouns:
    db_path = Path('words.csv')
    words = {}

    @classmethod
    def load_words(cls):
        if cls.db_path.exists():
            with cls.db_path.open('r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        cls.words[row[0]] = (row[1], row[2])

    @classmethod
    def save_words(cls, word1: str = None):
        if word1 is None:
            word1 = input('введите слово, согласующееся с числительным "один": ')
        word2 = input(f'введите слово, согласующееся с числительным "два": ')
        word5 = input(f'введите слово, согласующееся с числительным "пять": ')
        
        cls.words[word1] = (word2, word5)
        
        with cls.db_path.open('a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow([word1, word2, word5])

    @classmethod
    def pick(cls, number: int, word: str) -> str:
        if word not in cls.words:
            print(f'существительное "{word}" отсутствует в базе')
            cls.save_words(word)
        
        if 11 <= number % 100 <= 14:
            return cls.words[word][1]
        last_digit = number % 10
        if last_digit == 1:
            return word
        elif 2 <= last_digit <= 4:
            return cls.words[word][0]
        else:
            return cls.words[word][1]

CountableNouns.load_words()

#>>> CountableNouns.words
#{'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней')}
#>>> CountableNouns.pick(22, 'год')
#'года'
#>>> CountableNouns.pick(365, 'день')
#'дней'
#>>> CountableNouns.pick(21, 'попугай')
#существительное "попугай" отсутствует в базе
#введите слово, согласующееся с числительным "два": попугая
#введите слово, согласующееся с числительным "пять": попугаев
#'попугай'
#>>> CountableNouns.words
#{'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'попугай': ('попугая', 'попугаев')}
#>>> CountableNouns.save_words()
#введите слово, согласующееся с числительным "один": капля
#введите слово, согласующееся с числительным "два": капли
#введите слово, согласующееся с числительным "пять": капель
#>>> print(CountableNouns.db_path.read_text(encoding='utf-8'))
#год,года,лет
#месяц,месяца,месяцев
#день,дня,дней
#попугай,попугая,попугаев
#капля,капли,капель