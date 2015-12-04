## Local deployment instructions

1. Clone the repository

2. Create a virtualenv (optional)

  1. Install Virtualenv

            sudo apt-get install python-pip
            sudo pip install virtualenv

  2. Initialize a virtualenv

            virtualenv DeliDelux

  3. Activate the virtualenv

            cd DeliDelux/
            source bin/activate

3. Install Python dev

        sudo apt-get install python-dev

4. Install Libjpeg

        sudo apt-get install libjpeg8-dev

5.- Install  libxml2 and libxslt1
    sudo apt-get install libxml2-dev
    sudo apt-get install libxslt1-dev 

6. Install Django 1.8 and dependencies

        pip install -r requirements.txt

7. Comment the **haishin** app line in `haishin_project/settings.py` **INSTALLED_APPS** list

        python manage.py migrate

8. Uncomment previous line

        python manage.py makemigrations
        python manage.py migrate
        python manage.py createsuperuser

9. Run the server

        python manage.py runserver

10. Run the tests

        python manage.py test

That's all!

To test, you can install Chrome extension [POSTMAN 3](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) and import the `Haishin.json.postman_collection`.