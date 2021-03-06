﻿from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APISimpleTestCase, APIClient
from rest_framework.authtoken.models import Token
from haishin.models import *

# status: http://www.django-rest-framework.org/api-guide/status-codes/#successful-2xx

class ApiTests(APISimpleTestCase):

    def test_0_initialize_data(self):
        User.objects.create(id=1000,first_name="Kevin",last_name="Arriaga",username="admin",email="admin@haishin.com")
        Country.objects.create(id=1,name="Chile",code="CL")
        Country.objects.create(id=2,name="Argentina",code="AR")
        City.objects.create(id=1,country_id=1,name="Santiago",code="SCL")
        City.objects.create(id=2,country_id=2,name="Buenos Aires",code="BSAS")
        Town.objects.create(id=1,city_id=1,name="Providencia")
        Town.objects.create(id=2,city_id=1,name="Las Condes")
        Town.objects.create(id=3,city_id=2,name="Palermo")
        Town.objects.create(id=4,city_id=2,name="Recoleta")
        BusinessCategory.objects.create(id=1,name="Vegetariano")
        BusinessCategory.objects.create(id=2,name="Oriental")
        BusinessCategory.objects.create(id=3,name="Parrillas")
        BusinessCategory.objects.create(id=4,name="Marisquería")
        DishCategory.objects.create(id=1,name="Pastas")
        DishCategory.objects.create(id=2,name="Postres")
        DishCategory.objects.create(id=3,name="Mariscos")
        DishCategory.objects.create(id=4,name="Pescados")
        DishCategory.objects.create(id=5,name="Carnes")
        DishCategory.objects.create(id=6,name="Gourmet")
        DishAddonCategory.objects.create(id=1,name="Salsas",maximum=5)
        DishAddonCategory.objects.create(id=2,name="Ingredientes",maximum=3)

        Business.objects.create(id=1,admin_id=1000,category_id=3,name="La parrillada Uruguaya",town_id=1,address="Manuel Mont 870",latitude=-33.436571,longitude=-70.623346)
        Business.objects.create(id=2,admin_id=1000,category_id=1,name="Planta Maestra",town_id=2,address="Apoquindo 870",latitude=-33.436571,longitude=-70.623346)

        Dish.objects.create(id=1,business_id=1,category_id=5,name="Gran Parrillada",price=6500)
        Dish.objects.create(id=2,business_id=2,category_id=6,name="Festin Vegano",price=500)

        DishAddon.objects.create(id=1,name="Cebolla",price=1000,category_id=2,dish_id=2)
        DishAddon.objects.create(id=2,name="Lechuga",price=500,category_id=2,dish_id=2)

    def test_1_create_user(self):
        """
        Testing create new user
        """
        data = {
                'username': 'po5i',
                'password': 'haishin',
                'first_name': 'Carlos',
                'last_name': 'Villavicencio',
                'email': 'carlos.po5i@gmail.com',
                'profile': {
                            'address': 'Angamos 317'
                }
        }
        response = self.client.post('/api/user/',data, format='json')
        user = User.objects.get(username='po5i')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(user.username, 'po5i')

    def test_2_login(self):
        """
        Testing user login
        """
        data = {
                'username': 'po5i',
                'password': 'haishin'
        }
        response = self.client.post('/api-token/login/auth/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("token" in response.data, True)

    def test_3_update_profile(self):
        """
        Testing update profile
        """
        data = {
                'profile': {
                            'address': '111'
                }
        }

        user = User.objects.get(username='po5i')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.put('/api/user/' + str(user.id) + '/',data, format='json')
        user = User.objects.get(username='po5i')    #update object
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(user.profile.address, '111')


    def test_40_create_job(self):
        user = User.objects.get(username='po5i')
        data = {
                'user': user.id,
                'business': 2,
                'recipient_name': 'Carlos',
                'recipient_address': 'Angamos 317',
                'main_status': 'Draft',
                'delivery_status': '1',
                'remarks': 'Alergico a la soya',
                'details': '[{"dish":"2","quantity":"1","addons":[{"id":"1"},{"id":"2"}] }]',
                'delivery_date': '2015-12-18 15:05:00',
                'recipient_phone': '123456789',
                'total': '0',
                'recipient_latitude': '-33.436571',
                'recipient_longitude': '-70.623346'
        }
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post('/api/job/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user'], user.id)
        self.assertEqual(response.data['business'], 2)
        self.assertEqual(response.data['main_status'], 'Draft')
        self.assertEqual(response.data['recipient_name'], 'Carlos')
        self.assertEqual(response.data['details'][0]['id'], 1)

    def test_41_update_job_status(self):
        data = {
                'main_status': 'Received',
                'delivery_status': '2',
        }
        user = User.objects.get(username='po5i')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        job = Job.objects.get(user=user,business_id=2)
        response = self.client.patch('/api/job/' + str(job.id) + '/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['main_status'], 'Received')
        self.assertEqual(response.data['delivery_status'], '2')

    def test_42_update_job_status(self):
        data = {
                'main_status': 'Accepted',
                'delivery_status': '2',
        }
        user = User.objects.get(username='po5i')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        job = Job.objects.get(user=user,business_id=2)
        response = self.client.patch('/api/job/' + str(job.id) + '/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['main_status'], 'Accepted')
        self.assertEqual(response.data['delivery_status'], '2')

    def test_43_update_job_status(self):
        data = {
                'delivery_status': '5',
        }
        user = User.objects.get(username='po5i')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        job = Job.objects.get(user=user,business_id=2)
        response = self.client.patch('/api/job/' + str(job.id) + '/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['delivery_status'], '5')

    def test_44_update_job_status(self):
        data = {
                'delivery_status': '6',
        }
        user = User.objects.get(username='po5i')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        job = Job.objects.get(user=user,business_id=2)
        response = self.client.patch('/api/job/' + str(job.id) + '/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['delivery_status'], '6')

    def test_45_update_job_status(self):
        data = {
                'delivery_status': '7',
        }
        user = User.objects.get(username='po5i')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        job = Job.objects.get(user=user,business_id=2)
        response = self.client.patch('/api/job/' + str(job.id) + '/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['delivery_status'], '7')

    def test_5_filter_city(self):
        """
        Testing list of City by Country
        """
        data = {
                'code': 'CL'
        }
        response = self.client.get('/api/city/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Santiago')
        self.assertEqual(response.data[0]['id'], 1)

    def test_6_filter_business_city(self):
        """
        Testing list of Business by city id
        """
        data = {
                'city_id': 1
        }
        response = self.client.get('/api/business/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'La parrillada Uruguaya')
        self.assertEqual(response.data[0]['town'], 1)

    def test_7_filter_business_town(self):
        """
        Testing list of Business by town id
        """
        data = {
                'town_id': 2
        }
        response = self.client.get('/api/business/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Planta Maestra')
        self.assertEqual(response.data[0]['id'], 2)

    def test_8_filter_dish_business(self):
        """
        Testing list of dishes by business id
        """
        data = {
                'business_id': 2
        }
        response = self.client.get('/api/dish/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Festin Vegano')
        self.assertEqual(response.data[0]['price'], '500.00')

    def test_9_check_dish_group_by_business(self):
        data = {
                'business_id': 2
        }
        response = self.client.get('/util/dish/category/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Gourmet')
        self.assertEqual(response.data[0]['dishes'][0]['name'], 'Festin Vegano')
        self.assertEqual(response.data[0]['dishes'][0]['addons'][0]['name'], 'Ingredientes')
        self.assertEqual(response.data[0]['dishes'][0]['addons'][0]['items'][0]['name'], 'Cebolla')

