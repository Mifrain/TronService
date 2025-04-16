# 🚀 TronService

**TronService** — это микросервис на FastAPI, позволяющий получать информацию о Tron-адресах: баланс TRX, bandwidth, energy. Все запросы логируются в базу данных. Сервис поддерживает запуск в Docker и покрыт базовыми юнит и интеграционными тестами.

---

## 📌 Основной функционал

- Получение данных об адресе Tron по API.
- Запись информации о каждом запросе в базу данных.
- Получение списка всех сохранённых записей с поддержкой пагинации.
- Интеграция с Tron API через `tronpy`.
- Поддержка юнит и интеграционных тестов (`pytest`, `httpx`, `asyncpg`).

---

## 🧬 Структура проекта

```bash
├── app/
│   ├── main.py            # Точка входа FastAPI
│   ├── tron/              # Логика Tron (роуты, сервисы, схемы)
│   ├── database.py        # Настройка подключения к БД
│   └── config.py          # Настройки через .env
├── tests/
│   ├── unit_tests/        # Юнит-тесты
│   └── integration_test/  # Интеграционные тесты
├── alembic/               # Миграции базы данных
├── Dockerfile             # Docker-инструкция
├── docker-compose.yml     # Композиция сервисов
├── requirements.txt       # Зависимости проекта
├── init.sql               # Инициализация БД (в т.ч. тестовой)
└── .env                   # Конфигурация среды
```

---

## ⚙️ Установка и запуск

### 1. 📦 Клонирование репозитория

```bash
git clone https://github.com/Mifrain/TronService.git
cd TronService
```

### 2. ⚙️ Настройка переменных окружения

Создай `.env` файл (если его нет):

```bash
cp example.env .env
```

Заполни переменные окружения:

```env
MODE=DEV

DB_HOST=db
DB_PORT=5432
DB_USER=postgres
DB_PASS=postgres
DB_NAME=tronservice_db

TEST_DB_NAME=tronservice_test_db
TRON_API_KEY=your_tron_api_key_here
...
```

**Важно!** Получи [TRON_API_KEY](https://www.trongrid.io) для доступа к данным Tron.

### 3. 🐳 Запуск через Docker

Убедись, что установлен `Docker` и `docker-compose`, затем:

```bash
docker-compose up --build
```

Это:

- поднимет контейнер с PostgreSQL
- соберёт и запустит FastAPI-приложение по адресу http://localhost:8001

---

## 🔌 API Эндпоинты

### POST `/tron/`

Получает информацию об адресе в сети Tron и сохраняет в БД.

**Пример запроса:**

```http
POST /tron/?tron_address=TTestAddress123
```

### GET `/tron/`

Возвращает список сохранённых записей

### Swagger UI

Используйте Swagger UI для более удобного ручного тестирования
http://localhost:8001/docs

---

## 🧪 Тестирование

Проект содержит два типа тестов: юнит и интеграционные.

### 📥 Запуск тестов в Docker

```bash
docker-compose run --rm tron_app pytest app/tests
```

Тестовая база данных (`tronservice_test_db`) создаётся автоматически через `init.sql`.

---

## 🧠 Используемые технологии

- **FastAPI** — асинхронный веб-фреймворк
- **SQLAlchemy ORM** — для работы с БД
- **PostgreSQL** — основная база данных
- **Tronpy** — взаимодействие с Tron API
- **Pytest** — фреймворк для тестирования
- **Docker / Docker Compose** — контейнеризация
