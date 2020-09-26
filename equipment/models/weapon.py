""" Weapon model. """
from django.db import models

from .mixins import MagicItemModel
from .weapon_property import WeaponProperty


WEAPON_CATEGORY_CHOICES = [
    ('S', 'Simple Weapon'),
    ('M', 'Martial Weapon'),
    ('O', 'Other')
]


class Weapon(MagicItemModel):
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
    def can_use_dex(self):
        """ Property to determine if the weapon can use dexterity modifier """
        instance_properties = self.properties.all()
        finesse = self._check_for_name_in_properties('finesse', instance_properties)
        ranged = self._check_for_name_in_properties('ranged', instance_properties)
        thrown = self._check_for_name_in_properties('thrown', instance_properties)
        if finesse:
            return True
        if finesse and thrown:
            return True
        if not finesse and not thrown and ranged:
            return True
        return False

    @property
    def must_use_dex(self):
        """ Property to determine if the weapon must use dexterity modifier.
        Exclusively ranged weapons use dexterity """
        instance_properties = self.properties.all()
        finesse = self._check_for_name_in_properties('finesse', instance_properties)
        ranged = self._check_for_name_in_properties('ranged', instance_properties)
        thrown = self._check_for_name_in_properties('thrown', instance_properties)
        if not finesse and not thrown and ranged:
            return True
        return False

    @staticmethod
    def _check_for_name_in_properties(name, properties):
        property_names = [p.name.lower() for p in properties]
        for p_name in property_names:
            if name in p_name:
                return True
        return False

    def __str__(self):
        return 'Weapon: ' + str(self.name)
