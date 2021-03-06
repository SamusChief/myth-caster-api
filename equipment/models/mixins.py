""" Useful mixins for equipment models. """
from django.db import models

from .base_equipment import BaseEquipment

MUNDANE = 'M'
COMMON = 'C'
UNCOMMON = 'UC'
RARE = 'R'
VERY_RARE = 'VR'
LEGENDARY = 'L'
ARTIFACT = 'A'

RARITY_CHOICES = [
    (MUNDANE, 'Mundane'),
    (COMMON, 'Common'),
    (COMMON, 'Unommon'),
    (RARE, 'Rare'),
    (VERY_RARE, 'Very Rare'),
    (LEGENDARY, 'Legendary'),
    (ARTIFACT, 'Artifact')
]


class MagicItemModel(BaseEquipment):
    """
    Mixin class for adding rarity field and other magic item properties to an equipment.

    Attributes:
        rarity: the rarity level of the item, indicating rough power/cost.
            Default is Mundane ('M')
        requires_attunement: whether this magic item needs to be attuned to.
            Default is False.
    """

    rarity = models.CharField(choices=RARITY_CHOICES, default=MUNDANE, max_length=2, db_index=True)
    requires_attunement = models.BooleanField(default=False)

    @property
    def is_magic(self):
        """
        Helper property for items inheriting this to easily determine magical nature.

        Used since armor and weapons will all inherit this Mixin,
        and not all Armor and Weapons are magical.
        """
        return self.rarity is not MUNDANE

    class Meta:
        abstract = True
