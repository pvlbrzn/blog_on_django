from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Movie
from .forms import PostForm
from django.contrib import messages
from .services import parse_movies
from django.http import JsonResponse


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'main/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'main/post_detail.html', {'post': post})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пост опубликован')
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'main/add_post.html', {'form': form})


def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'main/movies_list.html', {'movies': movies})


def update_movies(request):
    if request.method == 'POST':
        try:
            parse_movies()  # Запускаем парсинг
            messages.success(request, "Фильмы успешно обновлены!")  # Успешное сообщение
        except Exception as e:
            messages.error(request, f"Ошибка при обновлении фильмов: {e}")  # Сообщение об ошибке

    return redirect('movies_list')  # Перенаправляем на страницу с фильмами