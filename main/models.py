from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    post_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title


class Movie(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название фильма")
    price = models.CharField(max_length=50, verbose_name="Цена билета")
    image_url = models.URLField(max_length=500, verbose_name="Картинка фильма", blank=True, null=True)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return f"{self.name} - {self.price}"
