# Wagtail-Tutorial

## Getting Started
- `pipenv shell`
- `wagtail start backend` 
- `cd backend`
- `pip install -r requirements.txt`
- `python manage.py migrate` set up database
- `python manage.py runserver` localhost8000
- `python manage.py createsuperuser`

## Create New Application (new page: news)
- `python manage.py startapp news`
- in `backend > settings > base.py` add news to INSTALLED_APPS list
- in `news > models.py`:
    - Create a new wagtail page
    - `python manage.py makemigrations`
    - `python.manage.py migrate`
- in /admin create a new child page. `news page` should be listed, with a title, intro, and body!

## Wagtail API v2
- add `wagtail.api.v2` to INSTALLED_APPS in `settings > base.py`
- configure endpoints/views
    - in the same folder as `urls.py` (backend folder) create a new file called `api.py`