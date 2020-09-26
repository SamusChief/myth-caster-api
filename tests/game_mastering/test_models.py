""" Unit Tests for the game_mastering.models module """
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase

from ddf import G

from game_mastering.models import Handout
from parties.models import Party


class PartiesUserMixinTestCase(APITestCase):
    """ Tests for the PartiesUserMixin class """
    def setUp(self):
        user_model = get_user_model()

        self.user_in_party_a = user_model.objects.create_user(username='user_in_party_a')
        self.user_in_party_b = user_model.objects.create_user(username='user_in_party_b')
        self.user_in_neither = user_model.objects.create_user(username='user_in_neither')
        self.game_master_a = user_model.objects.create_user(username='game_master_a')
        self.game_master_b = user_model.objects.create_user(username='game_master_b')

        self.party_a = G(Party, players=[self.user_in_party_a.id], \
            game_masters=[self.game_master_a.id])
        self.party_b = G(Party, players=[self.user_in_party_b.id], \
            game_masters=[self.game_master_b.id])

        self.handout_a = G(Handout, parties=[self.party_a.id])
        self.handout_b = G(Handout, parties=[self.party_b.id])
        self.handout_both = G(Handout, parties=[self.party_a.id, self.party_b.id])

    def test_parties_all_gms(self):
        """ Test that the parties_all_gms property grabs the game masters and not players """
        result_a = self.handout_a.parties_all_gms
        result_b = self.handout_b.parties_all_gms
        result_both = self.handout_both.parties_all_gms

        # GM A
        self.assertIn(self.game_master_a, result_a)
        self.assertNotIn(self.game_master_a, result_b)
        self.assertIn(self.game_master_a, result_both)

        # GM B
        self.assertNotIn(self.game_master_b, result_a)
        self.assertIn(self.game_master_b, result_b)
        self.assertIn(self.game_master_b, result_both)

        # User A
        self.assertNotIn(self.user_in_party_a, result_a)
        self.assertNotIn(self.user_in_party_a, result_b)
        self.assertNotIn(self.user_in_party_a, result_both)

        # User B
        self.assertNotIn(self.user_in_party_b, result_a)
        self.assertNotIn(self.user_in_party_b, result_b)
        self.assertNotIn(self.user_in_party_b, result_both)

        # User Neither
        self.assertNotIn(self.user_in_neither, result_a)
        self.assertNotIn(self.user_in_neither, result_b)
        self.assertNotIn(self.user_in_neither, result_both)

    def test_parties_all_players(self):
        """ Test that the parties_all_players property grabs the players and not game masters """
        result_a = self.handout_a.parties_all_players
        result_b = self.handout_b.parties_all_players
        result_both = self.handout_both.parties_all_players

        # GM A
        self.assertNotIn(self.game_master_a, result_a)
        self.assertNotIn(self.game_master_a, result_b)
        self.assertNotIn(self.game_master_a, result_both)

        # GM B
        self.assertNotIn(self.game_master_b, result_a)
        self.assertNotIn(self.game_master_b, result_b)
        self.assertNotIn(self.game_master_b, result_both)

        # User A
        self.assertIn(self.user_in_party_a, result_a)
        self.assertNotIn(self.user_in_party_a, result_b)
        self.assertIn(self.user_in_party_a, result_both)

        # User B
        self.assertNotIn(self.user_in_party_b, result_a)
        self.assertIn(self.user_in_party_b, result_b)
        self.assertIn(self.user_in_party_b, result_both)

        # User Neither
        self.assertNotIn(self.user_in_neither, result_a)
        self.assertNotIn(self.user_in_neither, result_b)
        self.assertNotIn(self.user_in_neither, result_both)

    def test_parties_all_users(self):
        """ Test that the parties_all_users property grabs all players and game masters """
        result_a = self.handout_a.parties_all_users
        result_b = self.handout_b.parties_all_users
        result_both = self.handout_both.parties_all_users

        # GM A
        self.assertIn(self.game_master_a, result_a)
        self.assertNotIn(self.game_master_a, result_b)
        self.assertIn(self.game_master_a, result_both)

        # GM B
        self.assertNotIn(self.game_master_b, result_a)
        self.assertIn(self.game_master_b, result_b)
        self.assertIn(self.game_master_b, result_both)

        # User A
        self.assertIn(self.user_in_party_a, result_a)
        self.assertNotIn(self.user_in_party_a, result_b)
        self.assertIn(self.user_in_party_a, result_both)

        # User B
        self.assertNotIn(self.user_in_party_b, result_a)
        self.assertIn(self.user_in_party_b, result_b)
        self.assertIn(self.user_in_party_b, result_both)

        # User Neither
        self.assertNotIn(self.user_in_neither, result_a)
        self.assertNotIn(self.user_in_neither, result_b)
        self.assertNotIn(self.user_in_neither, result_both)
