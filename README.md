# book-es-dsl-drf

## Installation

```
$ docker-compose up
```

### Run migrations and create indices

```
$ docker-compose run web python manage.py migrate
$ docker-compose run web python manage.py search_index --create
```

## Running project

```
$ xdg-open http://localhost:8000
```
