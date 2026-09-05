import requests
from bs4 import BeautifulSoup
import re

URL = "https://lemanapro.ru/catalogue/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/140 Safari/537.36"
}

print("Открываем каталог Лемана ПРО...")

response = requests.get(URL, headers=headers, timeout=30)

print("Код ответа сайта:", response.status_code)
print("Размер страницы:", len(response.text), "символов")

soup = BeautifulSoup(response.text, "lxml")

links = soup.find_all("a", href=True)

product_links = []

for link in links:
    href = link.get("href", "")
    if "/product/" in href:
        product_links.append(href)

product_links = list(dict.fromkeys(product_links))

print("Найдено ссылок на товары:", len(product_links))

for href in product_links[:10]:
    print("ТОВАР:", href)

print("Проверка закончена.")
