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

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/project-management-api.git
   cd project-management-api
   ```
2. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Apply the migrations:
    ```sh 
    python manage.py migrate
    ```

4. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```
5. Run the development server:
    ```sh
    python manage.py runserver
    ```