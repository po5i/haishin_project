## Local deployment instructions

1. Clone the repository

2. Create a virtualenv (optional)

3. Install Django 1.8 and dependencies
    ```
    pip install -r requirements.txt
    ```

4. Comment the 'haishin' app line in haishin_project/settings.py INSTALLED_APPS list
    ```
    python manage.py migrate
    ```

5. Uncomment previous line
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```

6. Run the server
    ```
    python manage.py runserver
    ```

That's all!
