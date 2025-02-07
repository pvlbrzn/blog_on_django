from django.core.management.base import BaseCommand
from main.services import parse_movies


class Command(BaseCommand):
    help = "Парсит фильмы с сайта 'https://bycard.by/' и сохраняет в БД"

    def handle(self, *args, **kwargs):
        try:
            parse_movies()
            self.stdout.write(self.style.SUCCESS('✅ Парсинг завершён успешно!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Ошибка парсинга: {e}'))
