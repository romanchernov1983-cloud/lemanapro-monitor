import requests

URL = "https://lemanapro.ru/catalogue/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8",
}

print("Открываем каталог Лемана ПРО...")

response = requests.get(URL, headers=headers, timeout=30)

print("Код ответа сайта:", response.status_code)
print("Размер ответа:", len(response.text), "символов")
print("Первые 500 символов ответа:")
print(response.text[:500])
