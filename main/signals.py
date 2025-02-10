from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Movie


@receiver(post_save, sender=Movie)
def movie_saved_signal(sender, instance, created, **kwargs):
    if created:
        print(f"✅ Новый фильм добавлен: {instance.name} - {instance.price}  - {instance.image_url}")
    else:
        print(f"✏️ Фильм обновлён: {instance.name}")
