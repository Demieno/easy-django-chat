# Django Chat ✌️ 🐍

![Django Logo](./static/images/logo-django.png "Django Logo")

Это шаблон простого одностраничного чата собранного на django, materialize.css
Установка зависимостей осуществляется используя Pipenv - 
[instructions](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)
Зависимости проекта находятся в Pipfile.

### Includes

* Django
* Materialize.css

### Data Base

В проект включенна поддержка Postgresql
Переключение можно делать путем нехитрых манипуляций в /chat/settings/dev.
В переменной DATABASES=[DATABASES_SQLITE3, DATABASES_PGSQL] выбираем одно из значений, 
после запускаем python manage.py makemigrations и migrate

### Template Structure


| Location                 |  Content                                   |
|--------------------------|--------------------------------------------|
| `/chat`                  | Django Project                             |
| `/chat/bd`               | Django Project Sqlite                            |
| `/chat/settings`         | Django Config                              |
| `/templates/index.html`  | Html Application Entry Point (`/`)         |
| `/static`                | Static Assets                              |


## Prerequisites

Перед началом работы вы должны установить и запустить следующее:

- [X] Python 3 - [instructions](https://wiki.python.org/moin/BeginnersGuide)
- [X] Pipenv - [instructions](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)

## Setup Template

```
$ git clone git@github.com:Demieno/easy-django-chat.git
$ cd easy-django-chat
```

## Setup
```
$ pipenv install && pipenv shell
$ cd chat
$ mkdir bd
$ python manage.py makemigrations
$ python manage.py migrate
```

## Running Development Servers

```
$ python manage.py runserver
```
