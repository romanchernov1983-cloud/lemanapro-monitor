import requests

URL = "https://lemanaprof.ru/catalogue/?page=1"

print("Проверяем внешний каталог...")

response = requests.get(URL, timeout=30)

print("Код ответа:", response.status_code)
print("Размер страницы:", len(response.text), "символов")
print("Первые 1000 символов:")
print(response.text[:1000])

print("Проверка закончена.")
