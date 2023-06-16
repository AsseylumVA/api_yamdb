
# YaMDb

Проект YaMDb собирает отзывы пользователей на различные произведения.


## Documentation

[Documentation](https://127.0.0.1:8000/redoc/)


## Installation

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:AsseylumVA/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
