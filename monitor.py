import requests
from bs4 import BeautifulSoup
import re

ARTICLE = "89366510"

url = f"https://www.google.com/search?q=site%3Alemanapro.ru+%22{ARTICLE}%22"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/140.0.0.0 Safari/537.36"
}

print("Ищем артикул:", ARTICLE)

response = requests.get(url, headers=headers, timeout=30)

print("Код ответа Google:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
text = soup.get_text(" ", strip=True)

matches = re.findall(r"\d[\d\s]*[₽р]\b", text)

print("Найденные цены:")
for price in matches[:20]:
    print(price)

print("Проверка закончена.")
