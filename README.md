# Django Celery SMS Queue
An asynchronous SMS sending service built with Django, Celery, and Redis.
SMS requests are queued and processed by background workers to avoid blocking the main application.

## Architecture
```
Client
  │
  ▼
Django View / API
  │
  ▼
Celery Queue (Redis)
  │
  ▼
Celery Worker
  │
  ▼
Kavenegar SMS Service
```
## Tech Stack
- Python

- Django

- Celery

- Redis

- Kavenegar SMS API

- Docker (optional)

## Environment Variables
Set the following environment variables before running the project
```
KAVENEGAR_API_KEY=your_kavenegar_api_key
SENDER_NUMBER=2000660110
```

## How it works
- The user submits a phone number via the form or API

- Django enqueues the SMS task using Celery

- The task is stored in Redis

- A Celery worker processes the task

- The SMS is sent via the Kavenegar service

## Running the Project Locally
```
pip install -r requirements.txt
```

## Start Redis
```
redis-server
```

## Run django
```
python3 manage.py runserver
```
## Run celery worker
```
celery -A core worker -l info
```

