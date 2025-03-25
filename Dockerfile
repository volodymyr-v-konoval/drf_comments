FROM python:3.10

WORKDIR /app
COPY . /app/

# Оновлюємо pip та встановлюємо Poetry
RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry install --no-interaction

# Створюємо папку для логів
RUN mkdir -p /app/logs && touch /app/logs/events.log && chmod -R 777 /app/logs

# Додаємо Gunicorn у PATH
RUN ln -s $(poetry env info --path)/bin/gunicorn /usr/local/bin/gunicorn

# Додаємо Python-шлях для Django
ENV PYTHONPATH=/app/simple_blog
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "simple_blog.wsgi:application"]
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "simple_blog.asgi:application"]
