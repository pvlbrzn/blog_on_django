from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('add_post/', views.add_post, name='add_post'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('movies/', views.movies_list, name='movies_list'),
    path('update_movies/', views.update_movies, name='update_movies'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movies_list/', include('movies.urls')),
]