from django.core.management.base import BaseCommand
from django_seed import Seed
from main.models import Post
from faker import Faker


class Command(BaseCommand):
    help = 'Генерация случайных данных для постов с помощью django-seeder и Faker'

    def handle(self, *args, **kwargs):
        fake = Faker("ru_RU")

        # Очистить ве существующие записи
        Post.objects.all().delete()

        # Настроим seed для создания объектов
        seeder = Seed.seeder()
        seeder.add_entity(Post, 10, {
            'title': lambda x: fake.sentence(nb_words=5),
            'content': lambda x: fake.sentence(nb_words=25),
            'author': lambda x: fake.name(),
        })

        # Запускаем генерацию данных и сохраняем их в БД
        inserted_pks = seeder.execute()

        self.stdout.write(self.style.SUCCESS("Тестовые посты успешно добавлены!!!"))