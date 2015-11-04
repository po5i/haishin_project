## Local deployment instructions

1. Clone the repository

2. Create a virtualenv (optional)
    2.1 Install Virtual env
        ```
        sudo pip install virtualenv
        ```
    2.2 Inicializate a virtual env
        ```
        virtualenv DeliDelux
        ```
    2.3 Activate the virtual env
        ```
        cd DeliDelux/
        source bin/activate
        ```


3. Install Python dev 
    ```
    sudo apt-get install python-dev
    ```

4. Install Libjpeg 
    ```
    sudo apt-get install libjpeg8-dev
    ```

5. Install Django 1.8 and dependencies
    ```
    pip install -r requirements.txt
    ```

6. Comment the 'haishin' app line in haishin_project/settings.py INSTALLED_APPS list
    ```
    python manage.py migrate
    ```

7. Uncomment previous line
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```

8. Run the server
    ```
    python manage.py runserver
    ```

That's all!

To test, you can install Chrome extension [POSTMAN 3](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) and import the `Haishin.json.postman_collection`.