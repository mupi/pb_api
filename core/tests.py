from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

class UserTests(APITestCase):

    def test_create_user(self):

		client = APIClient()
		response = client.post('/users/', {"username": "newidea", "password" : "123abc"}, format='json')
	#	self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #self.assertEqual(response.data, data)
