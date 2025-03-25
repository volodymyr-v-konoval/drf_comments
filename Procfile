web: gunicorn simple_blog.wsgi:application --chdir simple_blog --bind 0.0.0.0:$PORT
worker: celery -A simple_blog worker --loglevel=info
