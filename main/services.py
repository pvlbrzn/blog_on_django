import requests
from bs4 import BeautifulSoup as Bs
from .models import Movie
import time


def parse_movies():
    # Удаляем все записи перед обновлением
    Movie.objects.all().delete()

    # Парсим фильмы на сегодня
    timestamp = int(time.time())  # На сайте динамическая ссылка с датой и временем
    url = f'https://bycard.by/afisha/minsk/kino?btn_type=today&time={timestamp}'
    user_agent = (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    )

    response = requests.get(url, headers={"User-Agent": user_agent})
    if response.status_code != 200:
        raise RuntimeError(f"Ошибка: Не удалось получить HTML, статус: {response.status_code}")

    html = Bs(response.text, "lxml")
    container = html.select_one(
        "#page > main > section > div.marTopSection > div.dateEvents.home-row.by-type__row-category")

    if not container:
        raise ValueError("Ошибка: Контейнер с фильмами не найден, проверь HTML структуру!")

    items = container.select("a")

    for item in items:
        img = item.select_one("div > img")
        name_box = item.select_one("p.capsule__title")
        price_box = item.select_one("p.capsule__price")

        if name_box and price_box and img:
            name = name_box.text.strip()
            price = price_box.text.strip()
            image = img["src"].strip() if img.has_attr("src") else ""

            obj, created = Movie.objects.get_or_create(
                name=name,
                defaults={"price": price, "image_url": image}
            )
            # if created:
            #     print(f"✅ Добавлен новый фильм: {name} - {price} - {image}")
            # else:
            #     print(f"⚠️ Фильм уже существует: {name}")
        else:
            print(f"⚠️ Пропущен фильм (отсутствуют данные): {item}")
