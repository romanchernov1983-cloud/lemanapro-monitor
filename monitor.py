import requests
from bs4 import BeautifulSoup

URL = "https://lemanapro.ru/rooms/gostinaya/"

print("Открываем московскую страницу Лемана ПРО...")

response = requests.get(URL, timeout=30)

print("Код ответа сайта:", response.status_code)
print("Размер страницы:", len(response.text), "символов")

soup = BeautifulSoup(response.text, "lxml")

text = soup.get_text(" ", strip=True)

print("Найдена страница:", "Гостиная" in text)
print("Есть артикулы:", "Арт." in text)
print("Есть цены:", "₽" in text)

print("Проверка закончена.")
