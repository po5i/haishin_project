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
            sudo apt-get install libffi-dev
            sudo apt-get purge python-openssl
            sudo pip install pyopenssl

4. Install Libjpeg

            sudo apt-get install libjpeg8-dev

5. Install  libxml2 and libxslt1

            apt-get install libxml2-dev
            apt-get install libxslt1-dev 
            apt-get install python-libxml2
            apt-get install python-libxslt1

    Note: if you are using mac, dont forget to: xcode-select --install

6. Install Django 1.8 and dependencies

            pip install -r requirements.txt

    Note: if mac gives you problems when installing pusher you should execute:

            $ brew install pkg-config libffi
            $ export PKG_CONFIG_PATH=/usr/local/Cellar/libffi/3.0.13/lib/pkgconfig/

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

## Amazon Web Services deploy

To upload to AWS, just make a zip of all the project and `upload and deploy` to a new python 2.7 64 bits Elastic Beanstalk instance with a new Postgresql RDS, you will find the admin user with pasword haishin. Go to /admin and change it.

You can skip the static directory.

The frontend should point to this EBS endpoint.