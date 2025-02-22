from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies_list, name='movies_list'),
    path('movie/<int:movie_id>', views.movie_detail, name='movie_detail'),
    path('sessions/', views.session_list, name='session_list'),
    path('booking/<int:session_id>', views.book_ticket, name='book_ticket'),
    path('booking/success', views.booking_success, name='booking_success'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
