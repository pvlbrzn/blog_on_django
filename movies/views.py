from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Movie, Session
from .forms import BookingForm


# Страница с отображением всех фильмов
def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movies_list.html', context={"movies": movies})


# Детальная информация о фильме
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/movie_detail.html', context={'movie': movie})


# Список сеансов
def session_list(request):
    sessions = Session.objects.all()
    return render(request, 'movies/sessions_list.html', context={"sessions": sessions})


# Форма бронирования билетов
@login_required
def book_ticket(request, session_id):
    session = get_object_or_404(Session, id=session_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.session = session
            booking.total_price = booking.seats * session.price
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()

    return render(request, 'movies/booking_form.html', context={"form": form, "session": session})


# Страница успешного бронирования
def booking_success(request):
    return render(request, 'movies/booking_success.html')


# Представление для входа
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('movies_list')  # Перенаправляем на страницу фильмов
    else:
        form = AuthenticationForm()

    return render(request, 'movies/login.html', {'form': form})


# Представление для выхода
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Перенаправляем на страницу входа
