web: PYTHONPATH=. daphne -b 0.0.0.0 -p $PORT simple_blog.simple_blog.asgi:application
worker: celery -A simple_blog worker --loglevel=info
