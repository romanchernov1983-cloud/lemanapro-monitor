from playwright.sync_api import sync_playwright

URL = "https://lemanapro.ru/catalogue/"

print("Запускаем настоящий браузер Chromium...")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page(
        locale="ru-RU",
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
    )

    print("Открываем каталог Лемана ПРО...")

    response = page.goto(URL, wait_until="domcontentloaded", timeout=60000)

    print("Код ответа сайта:", response.status if response else "нет ответа")
    print("Заголовок страницы:", page.title())
    print("Текущий адрес:", page.url)

    page.wait_for_timeout(5000)

    print("Размер страницы:", len(page.content()), "символов")
    print("Первые 500 символов:")
    print(page.content()[:500])

    browser.close()

print("Проверка закончена.")
