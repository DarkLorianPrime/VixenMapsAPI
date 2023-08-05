# VixenMaps API
### About
Сервис, реализующий механику поиска адресов на картах с возможностью фильтрации по открытым\закрытым магазинам
# Built with
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

# RoadMap
- [x] Начать проект
- [x] Создать базовый функционал приложения (City, street)
- [x] Создать базовый функционал приложения (shop)
- [x] Добавить сортировку, фильтры
- [x] Добавить фильтр по открытым\закрытым магазинам
- [x] Запустить докер-компоуз
- [x] Причесать код
- [x] Написать тесты
- [x] Написать документацию

# Параметры
Доступные параметры фильтрации для /shop/:
- #### house (iexact)
- #### city (iexact)
- #### name (iexact)
- #### street (iexact)
- #### opened (0\1)

# Examples
В этом разделе будут рассмотрены примеры запросов. Больше примеров может быть найдено в tests

### Регистрация пользователя
#### POST /api/v1/city/
BODY 
```json
{
  "name": "Москва"
}
```
В случае успеха, ответ будет:

HTTP/1.1 201 Created
```json
{
  "id": "1",
  "name": "Москва"
}
```

#### POST /api/v1/city/1/street/
BODY
```json
{
  "name": "ул. Пушкина"
}
```
В случае успеха, ответ будет:

HTTP/1.1 201 Created
```json
{
    "id": 1,
    "name": "ул. Пушкина",
    "city_name": "Москва"
}

```

#### POST /api/v1/shop/
BODY
```json
{
    "id": 8,
    "name": "VixenSoft",
    "city": 1,
    "street": 1,
    "house": "д. Колотушкина",
    "open_time": "2:00",
    "close_time": "3:0"
}
```
В случае успеха, ответ будет:

HTTP/1.1 201 Created
```json
{
    "id": 1,
    "name": "VixenSoft",
    "city_name": "Москва",
    "street_name": "ул. Пушкина",
    "house": "д. Колотушкина",
    "open_time": "02:00:00",
    "close_time": "03:00:00"
}
```

#### GET /api/v1/shop/
###### ВВОДНЫЕ
сейчас: 02:30:00

QUERY
```json
{
  "opened": 1,
  "city": "мос",
  "street": "ул. пуш"
}
```
В случае успеха, ответ будет:

HTTP/1.1 200 OK
```json
{
    "id": 1,
    "name": "VixenSoft",
    "city_name": "Москва",
    "street_name": "ул. Пушкина",
    "house": "д. Колотушкина",
    "open_time": "02:00:00",
    "close_time": "03:00:00"
}
```

# Install
### Linux
Клонируем репозиторий:
```bash
$ git clone https://github.com/DarkLorianPrime/VixenMapsAPI
$ cd VixenMapsAPI
$ tree 
.
├── backend
│   ├── app
│   │   ├── cities
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── __init__.py
│   │   │   ├── migrations
│   │   │   │   ├── 0001_initial.py
│   │   │   │   └── __init__.py
│   │   │   ├── models.py
│   │   │   ├── repository.py
│   │   │   ├── serializers.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── core
│   │   │   ├── asgi.py
│   │   │   ├── __init__.py
│   │   │   ├── settings.py
│   │   │   ├── urls.py
│   │   │   └── wsgi.py
│   │   ├── manage.py
│   │   ├── poetry.lock
│   │   ├── pyproject.toml
│   │   └── shops
│   │       ├── admin.py
│   │       ├── apps.py
│   │       ├── filters.py
│   │       ├── __init__.py
│   │       ├── migrations
│   │       │   ├── 0001_initial.py
│   │       │   └── __init__.py
│   │       ├── models.py
│   │       ├── repositories.py
│   │       ├── serializers.py
│   │       ├── tests.py
│   │       ├── urls.py
│   │       └── views.py
│   ├── Dockerfile
│   └── entrypoint.sh
├── docker-compose.yaml
├── example.env
└── README.md
```
- Устанавливаем ENV
```bash
mv example.env .env
nano .env

--.env--
POSTGRES_USER=TEST
POSTGRES_HOST=database
POSTGRES_PASSWORD=TEST
POSTGRES_NAME=TEST
SECURITY_KEY=TEST
--------
```
- Запускаем docker-compose
```bash
$ docker-compose up -d --build
```
Вы должны увидеть надписи
```
Creating vixenmapsapi_database_1 ... done
Creating vixenmapsapi_backend_1  ... done
```

Сервис запущен и готов к работе. 
Остается только настроить `nginx`.

# Contacts
🦊 Grand developer - [@darklorianprime](https://vk.com/darklorianprime) - kasimov.alexander.ul@gmail.com