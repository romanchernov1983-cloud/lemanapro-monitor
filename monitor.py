import requests
from bs4 import BeautifulSoup
import re

URL = "https://lemanapro.ru/rooms/vodosnabzhenie-i-vodootvedenie/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/140.0.0.0 Safari/537.36"
}

print("Проверяем московскую категорию Лемана ПРО...")

response = requests.get(URL, headers=headers, timeout=30)

print("Код ответа:", response.status_code)
print("Размер страницы:", len(response.text))

soup = BeautifulSoup(response.text, "html.parser")
text = soup.get_text(" ", strip=True)

articles = re.findall(r"Арт\.\s*(\d{8})", text)
prices = re.findall(r"(\d[\d\s]*)\s*₽", text)

print("Найдено артикулов:", len(articles))
print("Найдено цен:", len(prices))

print("Первые артикулы:")
for article in articles[:10]:
    print(article)

print("Первые цены:")
for price in prices[:10]:
    print(price.strip())

print("Проверка закончена.")
