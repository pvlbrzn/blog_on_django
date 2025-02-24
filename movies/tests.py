from django.test import TestCase
from django.urls import reverse
from .models import Movie, Director, Actor, Genre


class MovieTestCase(TestCase):
    def setUp(self):
        """Создаём тестовые данные"""
        self.director = Director.objects.create(name="Кристофер Нолан", image="directors/nolan.jpg")
        self.actor = Actor.objects.create(name="Леонардо ДиКаприо", image="actors/leo.jpg")
        self.genre = Genre.objects.create(name="Фантастика")
        self.movie = Movie.objects.create(
            title="Начало",
            description="Фильм про сны",
            image="movies/inception.jpg",
            director=self.director,
            duration=148
        )
        self.movie.actors.add(self.actor)
        self.movie.genres.add(self.genre)

    def test_movie_creation(self):
        """Тест создания фильма"""
        movie = Movie.objects.get(title="Начало")
        self.assertEqual(movie.director.name, "Кристофер Нолан")
        self.assertTrue(self.actor in movie.actors.all())

    def test_movie_list_view(self):
        """Тест страницы списка фильмов"""
        response = self.client.get(reverse('movies_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Начало")
