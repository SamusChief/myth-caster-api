""" Unit Tests for the game_mastering.filters module """
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase, APIClient

from ddf import G

from game_mastering.models import Handout, Notes
from parties.models import Party


class HandoutFilterTestCase(APITestCase):
    """ Tests for the HandoutFilter class """
    def setUp(self):
        # set up client
        self.client = APIClient()

        # set up users: superuser, owner, editor, game_master, player, other
        user_model = get_user_model()
        self.superuser = user_model.objects.create_superuser(
            username='superuser', password='temp')
        self.owner = user_model.objects.create_user(username='owner', password='temp')
        self.editor = user_model.objects.create_user(username='editor', password='temp')
        self.game_master = user_model.objects.create_user(username='game_master', password='temp')
        self.player = user_model.objects.create_user(username='player', password='temp')
        self.other = user_model.objects.create_user(username='other', password='temp')

        # Create a handout: need a party for it as well
        self.party = G(Party, game_masters=[self.game_master.id], players=[self.player.id])
        self.handout = G(Handout, owner=self.owner, \
            authorized_editors=[self.editor.id], parties=[self.party.id])

    def test_owner_can_see_handout(self):
        """ Test that the marked owner can see the handout """
        self.client.login(username='owner', password='temp')

        response = self.client.get('/api/game_mastering/handouts/', format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json()['count'])
        self.assertEqual(self.handout.id, response.json()['results'][0]['id'])

    def test_editor_can_see_handout(self):
        """ Test that the marked editor can see the handout """
        self.client.login(username='editor', password='temp')

        response = self.client.get('/api/game_mastering/handouts/', format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json()['count'])
        self.assertEqual(self.handout.id, response.json()['results'][0]['id'])

    def test_game_master_can_see_handout(self):
        """ Test that the marked game_master can see the handout """
        self.client.login(username='game_master', password='temp')

        response = self.client.get('/api/game_mastering/handouts/', format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json()['count'])
        self.assertEqual(self.handout.id, response.json()['results'][0]['id'])

    def test_player_can_see_handout(self):
        """ Test that the marked player can see the handout """
        self.client.login(username='player', password='temp')

        response = self.client.get('/api/game_mastering/handouts/', format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json()['count'])
        self.assertEqual(self.handout.id, response.json()['results'][0]['id'])

    def test_other_user_cant_see_handout(self):
        """ Test that the other user cant see the handout """
        self.client.login(username='other', password='temp')

        response = self.client.get('/api/game_mastering/handouts/', format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()['count'])


class NotesFilterTestCase(APITestCase):
    """ Tests for the NotesFilter class """
    def setUp(self):
        # set up client
        self.client = APIClient()

        # set up users: superuser, owner, editor, game_master, player, other
        user_model = get_user_model()
        self.superuser = user_model.objects.create_superuser(
            username='superuser', password='temp')
        self.owner = user_model.objects.create_user(username='owner', password='temp')
        self.editor = user_model.objects.create_user(username='editor', password='temp')
        self.game_master = user_model.objects.create_user(username='game_master', password='temp')
        self.player = user_model.objects.create_user(username='player', password='temp')
        self.other = user_model.objects.create_user(username='other', password='temp')

        # Create a notes: need a party for it as well
        self.party = G(Party, game_masters=[self.game_master.id], players=[self.player.id])
        self.notes = G(Notes, owner=self.owner, \
            authorized_editors=[self.editor.id], parties=[self.party.id])

    def test_owner_can_see_notes(self):
        """ Test that the marked owner can see the notes """
        self.client.login(username='owner', password='temp')

        response = self.client.get('/api/game_mastering/notes/', format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json()['count'])
        self.assertEqual(self.notes.id, response.json()['results'][0]['id'])

    def test_editor_can_see_notes(self):
        """ Test that the marked editor can see the notes """
        self.client.login(username='editor', password='temp')

        response = self.client.get('/api/game_mastering/notes/', format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json()['count'])
        self.assertEqual(self.notes.id, response.json()['results'][0]['id'])

    def test_game_master_can_see_notes(self):
        """ Test that the marked game_master can see the notes """
        self.client.login(username='game_master', password='temp')

        response = self.client.get('/api/game_mastering/notes/', format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json()['count'])
        self.assertEqual(self.notes.id, response.json()['results'][0]['id'])

    def test_player_cant_see_notes(self):
        """ Test that the marked player can see the notes """
        self.client.login(username='player', password='temp')

        response = self.client.get('/api/game_mastering/notes/', format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()['count'])

    def test_other_user_cant_see_notes(self):
        """ Test that the other user cant see the notes """
        self.client.login(username='other', password='temp')

        response = self.client.get('/api/game_mastering/notes/', format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json()['count'])
