import requests
from bs4 import BeautifulSoup

# URL страницы
url = "http://www.world-art.ru/cinema/rating_top.php"

print("Запуск парсера...")

try:
    # Получаем HTML-код страницы
    response = requests.get(url)
    print(f"Статус ответа: {response.status_code}")

    if response.status_code == 200:
        print("Получен HTML-код страницы:")
        # Парсим HTML с помощью BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Ищем все строки таблицы с фильмами
        film_rows = soup.find_all('tr', height='20')  # Это строки, содержащие данные о фильмах

        for row in film_rows:
            cells = row.find_all('td')
            if len(cells) >= 5:  # Убедимся, что есть достаточное количество ячеек
                rank = cells[0].get_text(strip=True)  # Ранг фильма
                title = cells[1].get_text(strip=True)  # Название фильма
                score = cells[2].get_text(strip=True)  # Оценка
                votes = cells[3].get_text(strip=True)  # Количество голосов
                average_score = cells[4].get_text(strip=True)  # Средний балл

                print(f"Ранг: {rank}, Название: {title}, Оценка: {score}, Голосов: {votes}, Средний балл: {average_score}")
    else:
        print("Не удалось получить страницу.")
except requests.RequestException as e:
    print(f"Ошибка при запросе: {e}")
