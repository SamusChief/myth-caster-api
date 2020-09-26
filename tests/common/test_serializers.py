""" Unit tests for the common.serializers module """
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase, APIClient


SKILLS_PATH = '/api/skills/'


class OwnedModelSerializerTestCase(APITestCase):
    """ Tests for the OwnedModelSerialzier """
    def setUp(self):
        # Initialize client
        self.client = APIClient()

        # Initialize different POV users
        user_model = get_user_model()
        self.user = user_model.objects.create_user('user', password='temp')
        self.alternate_user = user_model.objects.create_user('alternate', password='temp')

    def test_no_owner_set_default_to_requester(self):
        """ Test that when no owner is set, defaults to current user making request """
        self.client.login(username='user', password='temp')

        skill_data = {
            'name': 'Athletics',
            'description': 'Perform physical checks like running, grabbing, and jumping',
            'ability': 'STR'
        }

        response = self.client.post(SKILLS_PATH, skill_data, format='json')
        print(response.json())
        self.assertEqual(201, response.status_code)
        response_owner = response.json()['owner']
        self.assertEqual(response_owner, self.user.id)

    def test_owner_override(self):
        """ Test that when owner is overridden, it is set properly """
        self.client.login(username='user', password='temp')

        skill_data = {
            'name': 'Athletics',
            'description': 'Perform physical checks like running, grabbing, and jumping',
            'ability': 'STR',
            'owner': self.alternate_user.id
        }

        response = self.client.post(SKILLS_PATH, skill_data, format='json')
        self.assertEqual(201, response.status_code)
        response_owner = response.json()['owner']
        self.assertEqual(response_owner, self.alternate_user.id)
