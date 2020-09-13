"""
Character model definition. Includes properties within the model which are derived from fields:
    - Modifier calculators for each of the 6 abilities
    - Complete inventory list
    - Complete proficiencies list
"""
import math

from django.core import validators
from django.db import models

from common.models import OwnedModel
from equipment.models import AdventuringGear, Armor, Tool, Weapon, WondrousItem
from skills.models import Skill

from .ancestry import Ancestry


class Character(OwnedModel):
    """
    Model for representing characters.
    """

    # Basic information fields
    name = models.CharField(max_length=255)
    ancestry = models.ForeignKey(to=Ancestry, on_delete=models.PROTECT)
    xp = models.PositiveIntegerField(default=0)
    level = models.IntegerField(default=1, validators=[validators.MinLengthValidator(1)])

    # Ability fields
    strength = models.PositiveIntegerField(default=10)
    dexterity = models.PositiveIntegerField(default=10)
    constitution = models.PositiveIntegerField(default=10)
    intelligence = models.PositiveIntegerField(default=10)
    wisdom = models.PositiveIntegerField(default=10)
    charisma = models.PositiveIntegerField(default=10)

    # Armor Proficiencies
    proficient_light_armor = models.BooleanField(default=False)
    proficient_medium_armor = models.BooleanField(default=False)
    proficient_heavy_armor = models.BooleanField(default=False)
    proficient_shields = models.BooleanField(default=False)

    # Weapon Proficiencies
    proficient_simple = models.BooleanField(default=False)
    proficient_martial = models.BooleanField(default=False)

    # Tool Proficiencies
    proficient_tools = models.TextField(default='')

    # Language Proficiencies
    proficient_languages = models.TextField(default='')

    # Skill Proficiencies
    proficient_skills = models.ManyToManyField(to=Skill)

    # catch all for other proficiencies, stored as comma delimited text
    proficient_other = models.TextField(default='')

    # Character Inventory Fields
    inventory_adventuring_gear = models.ManyToManyField(to=AdventuringGear)
    inventory_armors = models.ManyToManyField(to=Armor)
    inventory_tools = models.ManyToManyField(to=Tool)
    inventory_weapons = models.ManyToManyField(to=Weapon)
    inventory_wondrous_items = models.ManyToManyField(to=WondrousItem)

    @property
    def strength_modifier(self):
        """ Strength Modifier property """
        return Character._get_modifier(self.strength)

    @property
    def dexterity_modifier(self):
        """ Dexterity Modifier property """
        return Character._get_modifier(self.dexterity)

    @property
    def constitution_modifier(self):
        """ Constitution Modifier property """
        return Character._get_modifier(self.constitution)

    @property
    def intelligence_modifier(self):
        """ Intelligence Modifier property """
        return Character._get_modifier(self.intelligence)

    @property
    def wisdom_modifier(self):
        """ Wisdom Modifier property """
        return Character._get_modifier(self.wisdom)

    @property
    def charisma_modifier(self):
        """ Charisma Modifier property """
        return Character._get_modifier(self.charisma)

    @property
    def all_proficiencies(self):
        """ Get a characters full list of proficiencies. """
        result = []
        # TODO
        return result

    @property
    def all_inventory(self):
        """ Get a character's complete inventory """
        result = []
        result.extend(self.inventory_adventuring_gear.all())
        result.extend(self.inventory_armors.all())
        result.extend(self.inventory_tools.all())
        result.extend(self.inventory_weapons.all())
        result.extend(self.inventory_wondrous_items.all())
        return result

    @staticmethod
    def _get_modifier(score: int):
        """ Private method for calculating modifier based on score. """
        return math.floor((score - 10) / 2)
