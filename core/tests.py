from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Programa

class UserTests(APITestCase):

    def test_create_programa(self):

		client = APIClient()
		response = client.post('/programas/', {"id": "1", "titulo" : "programa de teste"}, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #self.assertEqual(response.data, data)
