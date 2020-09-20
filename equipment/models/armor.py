""" Armor model. """
from django.db import models

from .mixins import MagicItemModel


LIGHT = 'L'
MEDIUM = 'M'
HEAVY = 'H'
SHIELD = 'S'

ARMOR_CATEGORY_CHOICES = [
    (LIGHT, 'Light Armor'),
    (MEDIUM, 'Medium Armor'),
    (HEAVY, 'Heavy Armor'),
    (SHIELD, 'Shield')
]


class Armor(MagicItemModel):
    """
    Define armor model, and fields specific to Armor.

    Attributes:
        category: whether the armor is Light ('L'), Medium ('M'), Heavy ('H'), or a Shield ('S').
            Required.
        armor_class: The base armor class value, NOT the final calculated AC value. Required.
        strength_requirement: The Strength score requirement for wearing this armor.
            Default is 1 (no requirement)
        stealth_disadvantage: whether the armor imposes disadvantage on Stealth checks.
            Default is False
    """
    category = models.CharField(choices=ARMOR_CATEGORY_CHOICES, max_length=1, db_index=True)
    armor_class = models.IntegerField(db_index=True)
    strength_requirement = models.IntegerField(default=1)
    stealth_disadvantage = models.BooleanField(default=False)

    def __str__(self):
        return 'Armor: ' + str(self.name)
