from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('add_post/', views.add_post, name='add_post'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
]