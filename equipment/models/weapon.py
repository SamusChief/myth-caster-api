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
DEX_PROPERTY_KEYWORDS = ['finesse', 'thrown', 'ranged']


class Weapon(BaseEquipment, MagicItemMixin):
    """
    Model to represent weapons and their unique fields.

    Attributes:
        damage: a string representing the damage this weapon
        category: indicates what type of proficiency is needed to wield the weapon.
            One of: Simple ('S'), Martial ('M'), or Other ('O')
        properties: Relation field to WeaponProperty model. defaults to null.
    """
    damage = models.CharField(max_length=255, db_index=True)
    category = models.CharField(choices=WEAPON_CATEGORY_CHOICES, max_length=1, db_index=True)
    properties = models.ManyToManyField(to=WeaponProperty, related_name='weapons')

    @property
    def can_use_dex_mod(self):
        """ Property to determine if the weapon can use dexterity modifier """
        property_names = [p.name.lower() for p in self.properties.all()]
        for name in property_names:
            for keyword in DEX_PROPERTY_KEYWORDS:
                if keyword in name:
                    return True
        return False

    @property
    def must_use_dex_mod(self):
        """ Property to determine if the weapon must use dexterity modifier """
        property_names = [p.name.lower() for p in self.properties.all()]
        for name in property_names:
            if 'ranged' in name:
                return True
        return False
