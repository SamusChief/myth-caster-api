""" Skill model. """
from django.db import models

from common.models import OwnedModel

STRENGTH = 'STR'
DEXTERITY = 'DEX'
CONSTITUTION = 'CON'
INTELLIGENCE = 'INT'
WISDOM = 'WIS'
CHARISMA = 'CHA'
ABILITY_CHOICES = [
    (STRENGTH, 'Strength'),
    (DEXTERITY, 'Dexterity'),
    (CONSTITUTION, 'Constitution'),
    (INTELLIGENCE, 'Intelligence'),
    (WISDOM, 'Wisdom'),
    (CHARISMA, 'Charisma'),
]

class Skill(OwnedModel):
    """
    Model to represent skills and their unique attributes.

    Attributes:
        name: name of the skill.
        description: description of the skill, possibly including use examples.
    """
    name = models.CharField(unique=True, max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True)
    ability = models.CharField(choices=ABILITY_CHOICES, max_length=3)

    def __str__(self):
        return f'{self.ability}: {str(self.name)}'
