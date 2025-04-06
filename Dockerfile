FROM python:3.8-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . /app/

# Указываем переменную окружения для Django
ENV DATABASE_NAME=pavel
ENV DATABASE_USER=pavel
ENV DATABASE_PASSWORD=pavel

# Выполняем миграции и создаем суперпользователя
CMD ["sh", "-c", "python manage.py migrate && python manage.py loaddata test_data.json && python manage.py runserver 127.0.0.1:8000"]
