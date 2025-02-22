from django.contrib import admin
from .models import Actor, Director, Genre, Movie, Session, Booking


# Для модели Actor
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'image',)  # Показываем имя и изображение актера
    search_fields = ('name',)  # Добавляем возможность поиска по имени актера
    list_filter = ('name',)  # Добавляем фильтрацию по имени
    fieldsets = (
        (None, {
            'fields': ('name', 'image',)
        }),
    )
    verbose_name = 'Актер'
    verbose_name_plural = 'Актеры'


# Для модели Director
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'image',)  # Показываем имя и изображение режиссера
    search_fields = ('name',)  # Возможность поиска по имени режиссера
    list_filter = ('name',)  # Фильтрация по имени
    fieldsets = (
        (None, {
            'fields': ('name', 'image',)
        }),
    )
    verbose_name = 'Режиссер'
    verbose_name_plural = 'Режиссеры'


# Для модели Genre
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Показываем название жанра
    search_fields = ('name',)  # Возможность поиска по жанру
    list_filter = ('name',)  # Фильтрация по жанрам
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )
    verbose_name = 'Жанр'
    verbose_name_plural = 'Жанры'


# Для модели Movie
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'duration', 'get_actors',
                    'get_genres')  # Показываем название, режиссера, продолжительность, актеров и жанры
    search_fields = ('title', 'director__name')  # Поиск по названию и имени режиссера
    list_filter = ('director', 'genres')  # Фильтрация по режиссерам и жанрам

    # Функции для отображения актеров и жанров в списке фильмов
    def get_actors(self, obj):
        return ", ".join([actor.name for actor in obj.actors.all()])

    get_actors.short_description = 'Актеры'

    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])

    get_genres.short_description = 'Жанры'

    fieldsets = (
        (None, {
            'fields': ('title', 'director', 'duration', 'actors', 'genres', 'description', 'image')
        }),
    )
    verbose_name = 'Фильм'
    verbose_name_plural = 'Фильмы'


# Для модели Session
class SessionAdmin(admin.ModelAdmin):
    list_display = (
    'movie', 'datetime', 'available_seats', 'price')  # Показываем фильм, время сеанса, доступные места и цену
    search_fields = ('movie__title',)  # Поиск по названию фильма
    list_filter = ('movie', 'datetime')  # Фильтрация по фильму и времени сеанса
    fieldsets = (
        (None, {
            'fields': ('movie', 'datetime', 'available_seats', 'price')
        }),
    )
    verbose_name = 'Сеанс'
    verbose_name_plural = 'Сеансы'


# Для модели Booking
class BookingAdmin(admin.ModelAdmin):
    list_display = (
    'user', 'session', 'seats', 'total_price')  # Показываем пользователя, сеанс, количество мест и общую сумму
    search_fields = ('user__username', 'session__movie__title')  # Поиск по имени пользователя и названию фильма
    list_filter = ('session', 'user')  # Фильтрация по сеансу и пользователю
    fieldsets = (
        (None, {
            'fields': ('user', 'session', 'seats', 'total_price')
        }),
    )
    verbose_name = 'Бронирование'
    verbose_name_plural = 'Бронирования'


# Регистрация моделей
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Booking, BookingAdmin)
