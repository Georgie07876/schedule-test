# Расписание занятий

Фулстек-приложение для просмотра расписания занятий вуза: поиск по группе или преподавателю, недельная сетка с учётом чётности недели.

## Стек

**Backend:** Python, Django, Django REST Framework, django-filter, drf-spectacular (Swagger/Redoc), PostgreSQL, Redis (кэширование списка занятий)

**Frontend:** Vue 3, Quasar Framework, TypeScript, axios, dayjs

**Инфраструктура:** Docker, Docker Compose

## Требования

- Docker и Docker Compose

1. Склонировать репозиторий:

   ```bash
   git clone <URL_ВАШЕГО_РЕПОЗИТОРИЯ>
   cd <папка_проекта>
   ```

2. Создать файл окружения для бэкенда `backend/.env`:

   ```env
   SECRET_KEY=django-insecure-change-me-later-12345
   DEBUG=True
   ```

   DB_NAME=schedule_db
   DB_USER=schedule_user
   DB_PASSWORD=schedule123
   DB_HOST=postgres
   DB_PORT=5432

   REDIS_URL=redis://redis:6379/0

````

Значения переменных должны соответствовать тем, что реально читает `backend/config/settings/base.py` — сверьтесь с этим файлом, если название переменных отличается.

3. Поднять весь стек:

```bash
docker-compose up --build
````

Поднимутся сервисы: `backend` (Django, порт 8000), `postgres`, `redis`, `frontend` (nginx, порт 9000).

4. Применить миграции и наполнить БД тестовыми данными (в отдельном терминале, пока контейнеры работают):

   ```bash
   docker-compose exec backend python manage.py migrate
   docker-compose exec backend python manage.py seed_schedule
   docker-compose exec backend python manage.py createsuperuser
   ```

5. Открыть в браузере:
   - Фронтенд: http://localhost:9000
   - Swagger UI: http://localhost:8000/api/docs/
   - Redoc: http://localhost:8000/api/redoc/
   - Django Admin: http://localhost:8000/admin/

6. Проверить в строке поиска:
   -Долженко
   -Лозина
   -ПИ-341
