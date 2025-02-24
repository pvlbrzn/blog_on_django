from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from movies.models import Actor, Director, Genre, Movie, Session, Booking
from random import choice, randint
import random


class Command(BaseCommand):
    help = 'Generate fake data for the cinema app'

    def handle(self, *args, **kwargs):
        fake = Faker('ru_RU')

        # Создание фейковых актеров
        for _ in range(10):
            Actor.objects.create(
                name=fake.name(),
                image=fake.image_url()  # Убедитесь, что у вас настроен правильный путь для хранения изображений
            )

        # Создание фейковых режиссеров
        for _ in range(5):
            Director.objects.create(
                name=fake.name(),
                image=fake.image_url()
            )

        # Создание фейковых жанров
        genres = ['Боевик', 'Комедия', 'Драма', 'Ужасы', 'Мелодрама', 'Фантастика', 'Фэнтази']
        for genre_name in genres:
            Genre.objects.create(name=genre_name)

        # Создание фейковых фильмов
        directors = Director.objects.all()
        actors = Actor.objects.all()
        genres = Genre.objects.all()

        for _ in range(20):
            movie = Movie.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.text(),
                image=fake.image_url(),
                director=choice(directors),
                duration=randint(90, 180)  # Продолжительность в минутах
            )
            # Добавляем актеров и жанры
            movie.actors.set(random.sample(list(actors), randint(2, 5)))
            movie.genres.set(random.sample(list(genres), randint(1, 3)))  # Случайное количество жанров

        # Создание фейковых сеансов
        movies = Movie.objects.all()

        for _ in range(30):
            session = Session.objects.create(
                movie=choice(movies),
                datetime=fake.date_time_this_year(),
                available_seats=randint(50, 200),
                price=randint(300, 1000)  # Цена за сеанс
            )

        # Создание фейковых бронирований
        users = User.objects.all()
        sessions = Session.objects.all()

        for _ in range(50):
            user = choice(users)
            session = choice(sessions)
            seats = randint(1, 5)  # Сколько мест забронировано

            Booking.objects.create(
                user=user,
                session=session,
                seats=seats,
                total_price=seats * session.price
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated fake data!'))
