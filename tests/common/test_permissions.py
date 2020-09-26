""" Unit tests for the common.permissions module """
from django.contrib.auth import get_user_model

from ddf import G

from rest_framework.test import APITestCase, APIClient

from character.models import Character
from skills.models import Skill


IS_ADMIN_OR_READONLY_PATH = '/api/users/'
SKILLS_PATH = '/api/skills/'
CHARACTERS_PATH = '/api/characters/'


class IsAdminOrReadOnlyTestCase(APITestCase):
    """ Tests for the IsAdminOrReadOnly permissions class """
    def setUp(self):
        # Initialize client
        self.client = APIClient()

        # Initialize different POV users
        user_model = get_user_model()
        self.superuser = user_model.objects.create_superuser('superuser', password='temp')
        self.user = user_model.objects.create_user('user', password='temp')
        self.delete_target = user_model.objects.create_user('delete_target')

    def test_superuser_can_read(self):
        """ Test that a superuser can read data with this permission class """
        self.client.login(username='superuser', password='temp')

        response = self.client.get(f'{IS_ADMIN_OR_READONLY_PATH}')
        self.assertEqual(200, response.status_code)

    def test_superuser_can_create(self):
        """ Test that a superuser can create stuff on endpoints with this permission class """
        self.client.login(username='superuser', password='temp')

        response = self.client.options(f'{IS_ADMIN_OR_READONLY_PATH}')
        self.assertIn('POST', response.json()['actions'])

    def test_superuser_can_edit(self):
        """ Test that a superuser can edit stuff on endpoints with this permission class """
        self.client.login(username='superuser', password='temp')

        response = self.client.options(f'{IS_ADMIN_OR_READONLY_PATH}{self.user.id}/')
        self.assertIn('PUT', response.json()['actions'])

    def test_user_can_read(self):
        """ Test that a user can read data with this permission class """
        self.client.login(username='user', password='temp')

        response = self.client.get(f'{IS_ADMIN_OR_READONLY_PATH}')
        self.assertEqual(200, response.status_code)

    def test_user_cant_create(self):
        """ Test that a user cant create stuff on endpoints with this permission class """
        self.client.login(username='user', password='temp')

        response = self.client.options(f'{IS_ADMIN_OR_READONLY_PATH}')
        self.assertNotIn('actions', response.json())

    def test_user_cant_edit(self):
        """ Test that a user cant edit stuff on endpoints with this permission class """
        self.client.login(username='user', password='temp')

        response = self.client.options(f'{IS_ADMIN_OR_READONLY_PATH}{self.user.id}/')
        self.assertNotIn('actions', response.json())


class IsOwnerOrEditorTestCase(APITestCase):
    """ Tests for the IsOwnerOrEditor permissions class """
    def setUp(self):
        # Initialize client
        self.client = APIClient()

        # Initialize different POV users
        user_model = get_user_model()
        self.superuser = user_model.objects.create_superuser('superuser', password='temp')
        self.owner = user_model.objects.create_user('owner', password='temp')
        self.editor = user_model.objects.create_user('editor', password='temp')
        self.other_user = user_model.objects.create_user('other_user', password='temp')
        self.inactive_user = user_model.objects.create_user('inactive_user', \
            password='temp', is_active=False)

        self.skill = G(Skill, owner=self.owner, authorized_editors=[self.editor.id])
        self.private_character = G(Character, is_private=True, \
            owner=self.owner, authorized_editors=[self.editor.id])

    def test_anonymous_readonly(self):
        """ Anonymous users should be able to only read data """
        detail_response = self.client.get(f'{SKILLS_PATH}{self.skill.id}/', format='json')
        options_response_detail = self.client.options(f'{SKILLS_PATH}{self.skill.id}/', \
            format='json')

        self.assertEqual(200, detail_response.status_code)
        self.assertNotIn('actions', options_response_detail.json())

    def test_anonymous_403_for_private_content(self):
        """ Test that anonymous users cannot access private content """
        character_response = self.client.get(
            f'{CHARACTERS_PATH}{self.private_character.id}/', format='json')
        self.assertIn(character_response.status_code, [403, 404])

    def test_inactive_user_readonly(self):
        """ Test that an inactive user has read only access, like an anonymous user """
        self.client.login(username='inactive_user', password='temp')

        detail_response = self.client.get(f'{SKILLS_PATH}{self.skill.id}/', format='json')
        options_response_detail = self.client.options(f'{SKILLS_PATH}{self.skill.id}/', \
            format='json')

        self.assertEqual(200, detail_response.status_code)
        self.assertNotIn('actions', options_response_detail.json())

    def test_authenticated_user_can_read_and_post(self):
        """ Test that an authenticated user can create new data, and read data """
        self.client.login(username='other_user', password='temp')

        response = self.client.get(f'{SKILLS_PATH}', format='json')
        self.assertEqual(200, response.status_code)

        options = self.client.options(f'{SKILLS_PATH}', format='json')
        self.assertIn('POST', options.json()['actions'])

    def test_superuser_can_edit(self):
        """ Superusers should be able to edit data """
        self.client.login(username='superuser', password='temp')

        response = self.client.options(f'{SKILLS_PATH}{self.skill.id}/', format='json')
        self.assertIn('PUT', response.json()['actions'])

    def test_authenticated_non_owner_editor_user_cant_edit(self):
        """ Test that any authenticate users can create new data """
        self.client.login(username='other_user', password='temp')

        response = self.client.options(f'{SKILLS_PATH}{self.skill.id}/')
        self.assertNotIn('actions', response.json())

    def test_private_object_superuser_can_see(self):
        """ Test that for private objects, the superuser can edit """
        self.client.login(username='superuser', password='temp')

        get_response = self.client.get(f'{CHARACTERS_PATH}{self.private_character.id}/', \
            format='json')
        self.assertEqual(200, get_response.status_code)

    def test_private_object_owner_can_see(self):
        """ Test that for private objects, the owner can edit """
        self.client.login(username='owner', password='temp')

        get_response = self.client.get(f'{CHARACTERS_PATH}{self.private_character.id}/')
        self.assertEqual(200, get_response.status_code)

    def test_private_object_editor_can_see(self):
        """ Test that for private objects, the editor can edit """
        self.client.login(username='editor', password='temp')

        get_response = self.client.get(f'{CHARACTERS_PATH}{self.private_character.id}/', \
            format='json')
        self.assertEqual(200, get_response.status_code)

    def test_private_object_other_users_cant_see(self):
        """ Test that for private objects, other users cant edit """
        self.client.login(username='other_user', password='temp')

        get_response = self.client.get(f'{CHARACTERS_PATH}{self.private_character.id}/', \
            format='json')
        self.assertIn(get_response.status_code, [403, 404])
