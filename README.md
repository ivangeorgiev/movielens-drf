# MovieLens with Django Rest Framework

## Prepare environment

```bash
$ python -m venv .venv
$ source .venv/Scripts/activate
$ pip install requirements-dev.txt
$ python manage.py migrate
```

## Import MovieLens database

Donwload and unzip the latest 'small' database from https://grouplens.org/datasets/movielens/latest/ into `ml-latest-small` folder. Import the data using following commands:

```bash
$ python manage.py movielensimport movies ml-latest-small/movies.csv
$ python manage.py movielensimport links ml-latest-small/links.csv
```

If you need to reload the data, use the `--force` option.

## Start the development server

```bash
$ DJANGO_SETTINGS_MODULE=develop.settings python manage.py runserver
April 27, 2023 - 17:19:08
Django version 4.2, using settings 'develop.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
Open the Movie List API in a browser: http://127.0.0.1:8000/api/movies/
