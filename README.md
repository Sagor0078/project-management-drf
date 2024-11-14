# Project Management API

This is a Project Management API built with Django and Django REST Framework. It includes user authentication using Djoser and JWT, and provides endpoints for managing users, projects, and tasks.

## Features

- User authentication with Djoser (Token and JWT)
- CRUD operations for users, projects, and tasks
- API documentation with Swagger and Redoc

## Requirements

- Python 3.11
- Django 5.1.3
- Django REST Framework
- Djoser
- drf-yasg

## Installation


1. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

2. Apply the migrations:
    ```sh 
    python manage.py migrate
    ```

3. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```
4. Run the development server:
    ```sh
    python manage.py runserver
    ```
## API Documentation

1. **Swagger UI**:
    You can access the interactive Swagger UI documentation for the API at:
    ```sh
    http://127.0.0.1:8000/swagger/
    ```

2. **Redoc**:
    For an alternative view of the API documentation, you can use Redoc:
    ```sh
    http://127.0.0.1:8000/redoc/
    ```

These links will allow you to explore and test the API endpoints directly from the browser.
