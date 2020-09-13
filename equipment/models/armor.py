""" Armor """
from django.db import models

from .base_equipment import BaseEquipment
from .mixins import MagicItemMixin


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


class Armor(BaseEquipment, MagicItemMixin):
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
    category = models.CharField(choices=ARMOR_CATEGORY_CHOICES)
    armor_class = models.IntegerField()
    strength_requirement = models.IntegerField(default=1)
    stealth_disadvantage = models.BooleanField(default=False)
