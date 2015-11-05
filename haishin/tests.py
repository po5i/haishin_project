from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APISimpleTestCase, APIClient
from rest_framework.authtoken.models import Token
from haishin.models import *

# status: http://www.django-rest-framework.org/api-guide/status-codes/#successful-2xx

class ApiTests(APISimpleTestCase):

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
        response = self.client.post('/api/users/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'po5i')

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
                            'address': 'La Joya, Esmeralda'
                }
        }

        user = User.objects.get(username='po5i')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.put('/api/users/' + str(user.id) + '/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'po5i')