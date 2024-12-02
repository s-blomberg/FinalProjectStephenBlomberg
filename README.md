#### INF601 - Advanced Programming in Python
#### Stephen Blomberg
#### Final Project


# Final Project

## Description

This project will be using the Django framework to create a web app for a small business to track inventory and maintenance logs of items and equipment, as well as a weather API for the outdoor venue.

## Getting Started

### Dependencies

To download all requirements:

```
pip install -r requirements.txt
```

### Executing program

To create our data tables for migration, run in your terminal:
```
python manage.py makemigrations
```
To apply the migration, run in your terminal:
```
python manage.py migrate
```
To start the server, run in your terminal:
```
python manage.py runserver
```
To create an admin level account for login and admin panel access, run in your terminal:
```
python manage.py createsuperuser
```

After running the server, visit http://127.0.0.1:8000/ in your browser to launch the web-app.

### Output

This web-app allows user creation and authentication, inventory management with details for maintenance logging. As this small business operates primarily outdoors, I've included a weather API for the venue they operate at. 

## Authors

Stephen Blomberg

## Acknowledgments

Inspiration, code snippets, etc.
* [Jason Zeller](https://www.youtube.com/@profzeller)
* [Django](https://docs.djangoproject.com/en/5.0/)
* [Jinja](https://jinja.palletsprojects.com/en/stable/)
* [Bootstrap](https://getbootstrap.com/)
* [ChatGPT](https://chatgpt.com/share/672ceb52-2d48-8002-a176-5bbbc687c8ff)