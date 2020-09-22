""" Model to represent spells. """
from django.db import models

from character.models import CharacterClass
from common.models import OwnedModel

SAVE = 'S'
ROLL = 'R'
NONE = 'N'
SAVE_ROLL_CHOICES = [
    (SAVE, 'Saving Throw'),
    (ROLL, 'Roll a Spell Attack'),
    (NONE, 'None/Other')
]

ABJURATION = 'A'
CONJURATION = 'C'
DIVINATION = 'D'
ENCHANTMENT = 'EN'
EVOCATION = 'EV'
ILLUSION = 'I'
NECROMANCY = 'N'
TRANSMUTATION = 'T'
SPELL_SCHOOLS = [
    (ABJURATION, 'Abjuration'),
    (CONJURATION, 'Conjuration'),
    (DIVINATION, 'Divination'),
    (ENCHANTMENT, 'Enchantment'),
    (EVOCATION, 'Evocation'),
    (ILLUSION, 'Illusion'),
    (NECROMANCY, 'Necromancy'),
    (TRANSMUTATION, 'Transmutation')
]

class Spell(OwnedModel):
    """
    Spell model, with its unique attributes.
    """
    name = models.CharField(unique=True, max_length=255, db_index=True)
    description = models.TextField()
    school = models.CharField(choices=SPELL_SCHOOLS, max_length=2, db_index=True)
    save_or_roll = models.CharField(choices=SAVE_ROLL_CHOICES,
                                    default=NONE, max_length=1, db_index=True)
    damage = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    character_classes = models.ManyToManyField(to=CharacterClass)
