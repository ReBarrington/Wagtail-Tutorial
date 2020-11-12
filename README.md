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
    - copy and paste setup from doc
- Regiseter the URLS so Django can route requests into the API:
    - in `urls.py` add `path('api/v2/', api_router.urls),` to URL_PATTERNS
- add an api_fields list to `news > models.py`
- `http://localhost:8000/api/v2/pages/` shows pages API

## Integration
- axios.get('/api-of-backend') in frontend
- for every article in articles {}
- `news.NewsPage&fields=intro,body` specifies fields in api
- to avoid CORS error in developement: 
    - `pip install django-cors-headers`
    - `corsheaders` in base.py INSTALLED_APPS
    - add middleware
    - `CORS_ORIGIN_ALLOW_ALL = True` in base.py 
