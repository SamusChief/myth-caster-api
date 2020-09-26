""" Model for Parties, which are groups of players. """
from django.contrib.auth import get_user_model
from django.db import models

from common.models import OwnedModel


IN_PERSON = 'IP'
ONLINE = 'O'
BOTH = 'IP+B'
GAME_TYPES = [
    (IN_PERSON, 'In Person'),
    (ONLINE, 'Online'),
    (BOTH, 'Both In-Person and Online')
]

WEEKLY = 'W'
BIWEEKLY = 'BW'
MONTHLY = 'M'
HOLD = 'H'
OTHER = 'O'
GAME_FREQUENCIES = [
    (WEEKLY, 'Weekly'),
    (BIWEEKLY, 'Bi-Weekly'),
    (MONTHLY, 'Monthly'),
    (HOLD, 'On Hold'),
    (OTHER, 'Other'),
]


class Party(OwnedModel):
    """ Model to represent a game party. """
    name = models.CharField(unique=True, max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True)
    game_type = models.CharField(choices=GAME_TYPES, max_length=4, db_index=True)
    game_frequency = models.CharField(choices=GAME_FREQUENCIES, max_length=2, db_index=True)
    game_masters = models.ManyToManyField(to=get_user_model(), related_name='parties_gming')
    players = models.ManyToManyField(to=get_user_model(),
        blank=True, related_name='parties_playing')

    @property
    def all_users(self):
        """ Property to grab all distinct users """
        return (self.game_masters.all() | self.players.all()).distinct()
