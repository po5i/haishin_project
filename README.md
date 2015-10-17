1. Clone the repository

2. Install Django 1.8 and dependencies
    ```
    pip install Django
    pip install djangorestframework
    pip install django-cors-headers
    ```

3. Comment the 'haishin' app line in haishin_project/settings.py INSTALLED_APPS list
    ```
    cd (root django directory)
    python manage.py migrate
    ```

4. Uncomment previous line
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```

5. Run the server
    ```
    python manage.py runserver
    ```

That's all!