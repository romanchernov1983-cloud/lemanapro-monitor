import requests

URL = "https://lemanapro.ru/sitemap/"

print("Проверяем карту сайта Лемана ПРО...")

response = requests.get(URL, timeout=30)

print("Код ответа сайта:", response.status_code)
print("Размер страницы:", len(response.text), "символов")

print("Первые 1000 символов:")
print(response.text[:1000])

print("Проверка закончена.")
