# Welcome to Simple Blog!
Simple Blog is a single-page application (SPA) built with Django and Django REST Framework (DRF) on the backend, supporting real-time interactions via WebSockets. The platform allows users to write, comment, and interact with blog posts while ensuring security and efficiency.

## Features
- **User Authentication**: Secure login and session management with JWT.
- **Blog Management**: Users can create, edit, and delete blog posts.
- **Comments**: Users can comment on blog posts with real-time updates via WebSockets.
- **Search & Indexing**: OpenSearch integration for fast and efficient search functionality.
- **Security**: Protection against SQL injections, XSS attacks, and data leaks.
- **Docker Support**: The application is containerized for easy deployment.

## Technologies Used
- **Django** (backend framework)
- **Django ORM** (database interaction via ORM)
- **Django REST Framework** (API development)
- **PostgreSQL** (database)
- **Redis** (caching and WebSockets support)
- **WebSockets** (real-time data updats)
- **OpenSearch** (full-text search and indexing)
- **Celery** (asynchronous task queue)
- **Queue** (task queue processing via Celery and RabbitMQ)
- **Cache** (performance optimization with Redis caching)
- **Events** (event handling and Django signals)
- **JWT** (secure authentication)
- **RabbitMQ** (message broker for Celery)
- **Docker** (containerization)
- **Git** (version control)
- **Koyeb** (cloud hosting and automatic deployment)





## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Requirements
Before you start, ensure you have:
- Python 3.10+
- Poetry (dependency management)
- Docker
- PostgreSQL
- Redis
- OpenSearch
- RabbitMQ
- Celery

## Installation
1. Clone the repository:
```bash
git clone https://github.com/volodymyr-v-konoval/drf_comments
```
2. Navigate to the project directory:
```bash
cd simple_blog
```
3. Set up a virtual environment:
```bash
poetry install
poetry shell
```
4. Create a `.env` file and configure the required environment variables. Use `.env_example` as a reference.

5. Run the database using Docker:
```bash
docker compose up -d
```
6. Apply migrations to set up the database:
```bash
python3 manage.py migrate
```
7. Create a superuser:
```bash
python3 manage.py createsuperuser
```

## Usage
To start the application, run:
```bash
python3 manage.py runserver
```
The API will be available at `http://127.0.0.1:8000/`

To rebuild OpenSearch indices, use:
```bash
python3 manage.py opensearch document index
```

## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Implement your changes.
4. Push your branch: `git push origin feature-name`.
5. Create a pull request.

## Authors
[@volodymyr-v-konoval](https://github.com/volodymyr-v-konoval) and contributors.

## License
© 2025

_This README was generated with ❤️ by the author._

