# FastAPI + MongoDB - приложение для хранения и обработки данных

## ТЗ

* Реализовать веб-приложение, которое предоставляет собой REST API 
для записи в БД данных посредством POST-запросов из подключаемого на сайт
модуля в JSON формате.
* Реализовать GET-запрос на получение данных в JSON-формате.
* Реализовать GET-запрос на получение визуализированных данных.

## Необходимые инструменты

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [GNU Make](https://www.gnu.org/software/make/)

## Запуск

1. **Склонировать репозиторий:**

   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository

2. Установить Docker, Docker-compose, Makefile пакеты.

3. Создать в корневой папке проекта файл `.env`, в котором нужно задать 
переменные окружения, по аналогии с файлом `.env.example`
```
DB_HOST=
DB_PORT=
DB_NAME=
APP_HOST=
APP_PORT=
MONGO_EXPRESS_HOST=
MONGO_EXPRESS_PORT=
MONGO_DB_ADMIN_USERNAME=
MONGO_DB_ADMIN_PASSWORD=
```

### Реализованные команды

* **`make all` - поднять все приложение целиком**
* `make app` - поднять только приложение
* `make storage` - поднять только базу данных


* **`make all-down` - остановить все приложение целиком**
* `make app-down` - остановить контейнер с приложением
* `make storage-down` - остановить контейнер с базой


* `make app-logs` - смотреть логи в контейнере с приложением
* `make app-shell` - зайти в баш-консоль контейнера с приложением

4. Запустить контейнеры с приложением
```bash
   make all
```
5. Заполнить базу тестовыми данными
```bash
make app-shell

ipython fill_database.py
```

### По дефолту .env.example

* Swagger: localhost:8000/api/docs
* MongoDB: localhost:27017
* MongoExpress (UI): localhost:28081