""" Unit Tests for the characters.filters module """
from django.contrib.auth import get_user_model

from ddf import G

from rest_framework.test import APITestCase, APIClient

from character.models import Character

PRIVATE_COUNT = 1
PUBLIC_COUNT = 1
ALL_COUNT = PRIVATE_COUNT + PUBLIC_COUNT


class CharacterOwnedOrAdminFilterTestCase(APITestCase):
    """ Tests of the CharacterOwnedOrAdminFilter, to ensure it
    is filtering out private characters unless the requester
    owns it, can edit it, or is an admin. """
    def setUp(self):
        # Initialize client
        self.client = APIClient()

        # Initialize different POV users
        user_model = get_user_model()
        self.superuser = user_model.objects.create_superuser('superuser', password='temp')
        self.owner = user_model.objects.create_user('owner', password='temp')
        self.editor = user_model.objects.create_user('editor', password='temp')
        self.some_user = user_model.objects.create_user('some_user', password='temp')

        # create some test users
        G(Character, PRIVATE_COUNT, owner=self.owner, \
            authorized_editors=[self.editor.id], is_private=True)
        G(Character, PUBLIC_COUNT, owner=self.owner, \
            authorized_editors=[self.editor.id], is_private=False)

    def test_superuser_should_see_all(self):
        """ Test that superusers are shown all characters regardless """
        self.client.login(username='superuser', password='temp')
        response = self.client.get('/api/characters/', format='json')

        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json()['count'], ALL_COUNT)

    def test_owner_should_see_all(self):
        """ Test that owner of characters can see all """
        self.client.login(username='owner', password='temp')
        response = self.client.get('/api/characters/', format='json')

        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json()['count'], ALL_COUNT)

    def test_editor_should_see_all(self):
        """ Test that editor of characters can see all """
        self.client.login(username='editor', password='temp')
        response = self.client.get('/api/characters/', format='json')

        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json()['count'], ALL_COUNT)

    def test_other_user_should_see_public(self):
        """ Test that other users can see public """
        self.client.login(username='other_user', password='temp')
        response = self.client.get('/api/characters/', format='json')

        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json()['count'], PUBLIC_COUNT)
