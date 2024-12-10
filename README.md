#### INF601 - Advanced Programming in Python
#### Stephen Blomberg
#### Final Project


# Final Project

## Description

This project will be using the Django framework to create a web app for a small business to track inventory and maintenance logs of items and equipment, as well as a weather API as they frequently operate outdoors.

## Getting Started

### Dependencies

To download all requirements:

```
pip install -r requirements.txt
```

### Executing program

To create the migration files for the database, run in your terminal:
```
python manage.py makemigrations
```
To apply the migrations to the database, run in your terminal:
```
python manage.py migrate
```
To create an admin level account for login and admin panel access, run in your terminal:
```
python manage.py createsuperuser
```
To start the server, run in your terminal:
```
python manage.py runserver
```

After running the server, visit http://127.0.0.1:8000/ in your browser to launch the web-app.

### Output

This web-app allows user creation and authentication, inventory management, and maintenance logging. As this small business operates primarily outdoors, I've included a weather API to display weather conditions. 

## Authors

Stephen Blomberg

## Acknowledgments

Inspiration, code snippets, etc.
* [Jason Zeller](https://www.youtube.com/@profzeller)
* [Django](https://docs.djangoproject.com/en/5.0/)
* [Jinja](https://jinja.palletsprojects.com/en/stable/)
* [Bootstrap](https://getbootstrap.com/)
* [AccuWeather](https://developer.accuweather.com/)
* [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
* [ChatGPT](https://chatgpt.com/share/674e43eb-8b44-8002-a965-168b4ffb2b90)