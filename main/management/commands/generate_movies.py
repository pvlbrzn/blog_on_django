from django.core.management.base import BaseCommand
from django_seed import Seed
from main.models import Movie
from faker import Faker


class Command(BaseCommand):
    help = 'Генерация случайных данных для фильмов с помощью django-seeder и Faker'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Очистить все существующие записи
        Movie.objects.all().delete()

        # Настроим сидера для создания объектов
        seeder = Seed.seeder()
        seeder.add_entity(Movie, 10, {
            'name': lambda x: fake.sentence(nb_words=3),
            'price': lambda x: f"{fake.random_int(min=5, max=20)} BYN",
            'image_url': lambda x: f"https://via.placeholder.com/300x400?text={fake.word()}",
        })

        inserted_pks = seeder.execute()

        self.stdout.write(self.style.SUCCESS("✅ Тестовые фильмы успешно добавлены!"))
