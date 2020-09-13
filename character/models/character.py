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
        """ Strength Modifier property. Returns an integer. """
        return Character._get_modifier(self.strength)

    @property
    def dexterity_modifier(self):
        """ Dexterity Modifier property. Returns an integer. """
        return Character._get_modifier(self.dexterity)

    @property
    def constitution_modifier(self):
        """ Constitution Modifier property. Returns an integer. """
        return Character._get_modifier(self.constitution)

    @property
    def intelligence_modifier(self):
        """ Intelligence Modifier property. Returns an integer. """
        return Character._get_modifier(self.intelligence)

    @property
    def wisdom_modifier(self):
        """ Wisdom Modifier property. Returns an integer. """
        return Character._get_modifier(self.wisdom)

    @property
    def charisma_modifier(self):
        """ Charisma Modifier property. Returns an integer. """
        return Character._get_modifier(self.charisma)

    @property
    def all_proficiencies_list(self):
        """ Get a characters full list of proficiencies. """
        result = []
        armor, weapons, tools, languages, skills, other = self._get_proficiencies()

        result.extend(armor)
        result.extend(weapons)
        result.extend(tools)
        result.extend(languages)
        result.extend(skills)
        result.extend(other)

        return result

    @property
    def all_proficiencies_dict(self):
        """ Get a characters full list of proficiencies, formatted as a dict object. """
        armor, weapons, tools, languages, skills, other = self._get_proficiencies()

        return {
            'armor': armor,
            'weapons': weapons,
            'tools': tools,
            'languages': languages,
            'skills': skills,
            'other': other,
        }

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

    def _get_proficiencies(self):
        """
        Grab and return the various proficiencies a character has.

        :return: a tuple of proficiency arrays, in this order:
            armor, weapons, tools, languages, skills, other
        """
        # Armor proficiencies
        armor_proficiencies = []
        if self.proficient_light_armor:
            armor_proficiencies.append('Light Armor')
        if self.proficient_medium_armor:
            armor_proficiencies.append('Medium Armor')
        if self.proficient_heavy_armor:
            armor_proficiencies.append('Heavy Armor')
        if self.proficient_light_armor:
            armor_proficiencies.append('Shields')
        armor_proficiencies = sorted(armor_proficiencies)

        # Weapon proficiencies
        weapon_proficiencies = []
        if self.proficient_simple:
            armor_proficiencies.append('Simple')
        if self.proficient_martial:
            armor_proficiencies.append('Martial')
        weapon_proficiencies = sorted(weapon_proficiencies)

        # Other proficiencies
        tool_proficiencies = sorted(self.proficient_tools.split(','))
        language_proficiencies = sorted(self.proficient_languages.split(','))
        other_proficiencies = sorted(self.proficient_other.split(','))

        # Skill proficiencies
        skill_proficiencies = []
        for skill in self.proficient_skills:
            skill_proficiencies.append(skill.name)
        skill_proficiencies = sorted(skill_proficiencies)

        return armor_proficiencies, weapon_proficiencies, tool_proficiencies, \
               language_proficiencies, skill_proficiencies, other_proficiencies
