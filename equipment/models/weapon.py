""" Weapon model. """
from django.db import models

from .base_equipment import BaseEquipment
from .mixins import MagicItemMixin
from .weapon_property import WeaponProperty


WEAPON_CATEGORY_CHOICES = [
    ('S', 'Simple Weapon'),
    ('M', 'Martial Weapon'),
    ('O', 'Other')
]


class Weapon(BaseEquipment, MagicItemMixin):
    """
    Model to represent weapons and their unique fields.

    Attributes:
        damage_dice: a string representing the base damage dice this weapon deals.
        damage_type: a string representing the type of damage this weapon deals on hit.
        category: indicates what type of proficiency is needed to wield the weapon.
            One of: Simple ('S'), Martial ('M'), or Other ('O')
        properties: Relation field to WeaponProperty model. defaults to null.
    """
    damage_dice = models.CharField(max_length=255, db_index=True)
    damage_type = models.CharField(max_length=255, db_index=True)
    category = models.CharField(choices=WEAPON_CATEGORY_CHOICES, max_length=1, db_index=True)
    properties = models.ManyToManyField(to=WeaponProperty, related_name='weapons')
