web: daphne -b 0.0.0.0 -p 8000 simple_blog.asgi:application --chdir simple_blog
worker: celery -A simple_blog worker --loglevel=info
