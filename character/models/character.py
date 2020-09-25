"""
Character model definition. Includes properties within the model which are derived from fields:
    - Modifier calculators for each of the 6 abilities
    - Complete inventory list
    - Complete proficiencies list
"""
import math

from django.db import models

from common.models import OwnedModel
from equipment.models import AdventuringGear, Armor, Tool, Weapon, WondrousItem
from skills.models import Skill
from conditions.models import Condition

from .ancestry import Ancestry, SubAncestry
from .background import Background
from .character_class import CharacterClass

PROFICIENT = 'P'
EXPERT = 'E'
PROFICIENCY_LEVELS = [
    (PROFICIENT, 'Proficient'),
    (EXPERT, 'Expert'),
]


class ClassAndLevel(OwnedModel):
    """ Mapping table for tracking a character's class and level in that class. """
    character_class = models.ForeignKey(to=CharacterClass, on_delete=models.PROTECT)
    level = models.PositiveIntegerField()


class InventoryAdventuringGear(OwnedModel):
    """ Mapping table for tracking a characters gear and quantities """
    gear = models.ForeignKey(to=AdventuringGear, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()


class InventoryArmor(OwnedModel):
    """ Mapping table for tracking a characters armors and quantities """
    gear = models.ForeignKey(to=Armor, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()


class InventoryTool(OwnedModel):
    """ Mapping table for tracking a characters tools and quantities """
    gear = models.ForeignKey(to=Tool, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()


class InventoryWeapon(OwnedModel):
    """ Mapping table for tracking a characters weapons and quantities """
    gear = models.ForeignKey(to=Weapon, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()


class InventoryWondrousItem(OwnedModel):
    """ Mapping table for tracking a characters wondroud items and quantities """
    gear = models.ForeignKey(to=WondrousItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()


class SkillProficiency(OwnedModel):
    """ Mapping table for tracking skill and proficiency level """
    skill = models.ForeignKey(to=Skill, on_delete=models.PROTECT)
    proficiency_level = models.CharField(choices=PROFICIENCY_LEVELS,
                                         default=PROFICIENT, max_length=1)


class Character(OwnedModel):
    """
    Model for representing characters.

    Attributes:
        name: name of the character
        ancestry: the character's ancestry
        background: the character's background
        xp: total experience points
        class_levels: mapping of classes and levels the character has
        is_private: whether this character should be publicly accessible. Default to False
        hit_point_total: character total hit points
        hit_point_current: character current hit points
        conditions: character's current conditions affecting them
        temporary_hit_point_total: temporary HP, deducted first
        strength: raw physical strength of the character
        dexterity: agility and poise of the character
        constitution: toughness and durability of the character
        intelligence: raw intellect and knowledge of the character
        wisdom: instincts and self-knowledge of the character
        charisma: personality and charm of the character
        proficient_light_armor: whether the character can use light armor
        proficient_heavy_armor: whether the character can use heavy armor
        proficient_shields: whether the character can use shields
        proficient_simple: whether the character can use simple weapons
        proficient_martial: whether the character can use martial weapons
        proficient_tools: which tools the character can use
        proficient_languages: which languages the character can speak/read/write
        proficient_other: any other proficiencies the character has
        skills: mapping of skills and proficiency levels the character has
        jack_of_all_trades: whether the user gains half their proficiency bonus
        misc_initiative_bonus: any miscellaneous bonuses to initiative
        inventory_adventuring_gear: mapping to quantity and gear items
        inventory_armor: mapping to quantity and armors
        inventory_tools: mapping to quantity and tools
        inventory_weapons: mapping to quantity and weapons
        inventory_wondroud_items: mapping to quantity and wondrous items
    """
    # Basic information fields
    name = models.CharField(max_length=255, db_index=True)
    ancestry = models.ForeignKey(to=Ancestry, on_delete=models.PROTECT, \
        related_name='characters_with_ancestry')
    subancestry = models.ForeignKey(to=SubAncestry, on_delete=models.PROTECT, \
        related_name='characters_with_subancestry', blank=True, null=True)
    background = models.ForeignKey(to=Background, on_delete=models.PROTECT)
    xp = models.PositiveIntegerField(default=0)
    class_levels = models.ManyToManyField(to=ClassAndLevel, blank=True, \
        related_name='characters_with_class_and_level')
    is_private = models.BooleanField(default=False)

    # Health, conditions, and death tracking
    hit_point_total = models.PositiveIntegerField()
    hit_point_current = models.PositiveIntegerField()
    temporary_hit_point_total = models.PositiveIntegerField()
    conditions = models.ManyToManyField(to=Condition, blank=True, \
        related_name='characters_with_condition')

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
    proficient_tools = models.TextField(blank=True, null=True)

    # Language Proficiencies
    proficient_languages = models.TextField(blank=True, null=True)

    # Skill Proficiencies
    skills = models.ManyToManyField(to=SkillProficiency, blank=True,
                                    related_name='characters_with_skill_proficiency')
    jack_of_all_trades = models.BooleanField(default=False)
    misc_initiative_bonus = models.PositiveIntegerField(default=0)

    # catch all for other proficiencies, stored as comma delimited text
    proficient_other = models.TextField(blank=True, null=True)

    # Character Inventory Fields
    inventory_adventuring_gear = models.ManyToManyField(to=InventoryAdventuringGear, blank=True,
                                                        related_name='characters_with_gear')
    inventory_armors = models.ManyToManyField(to=InventoryArmor, blank=True,
                                              related_name='characters_with_armor')
    inventory_tools = models.ManyToManyField(to=InventoryTool, blank=True,
                                             related_name='characters_with_tool')
    inventory_weapons = models.ManyToManyField(to=InventoryWeapon, blank=True,
                                               related_name='characters_with_weapon')
    inventory_wondrous_items = models.ManyToManyField(to=InventoryWondrousItem, blank=True,
                                                      related_name='characters_with_wondrous_item')

    @property
    def proficiency_bonus(self):
        """ Get total character levels, and convert it to a proficiency bonus """
        total_level = 0
        for class_level in self.class_levels.all():
            total_level += class_level.level

        return math.ceil((total_level / 4) + 1)

    @property
    def initiative(self):
        """ Get initiative, factoring bonuses and jack of all trades. """
        result = 0
        result += self.dexterity_modifier
        if self.jack_of_all_trades:
            result += math.floor(self.proficiency_bonus / 2)
        result += self.misc_initiative_bonus
        return result

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
        for skill in self.skills.all():
            skill_proficiencies.append(skill.skill.name)
        skill_proficiencies = sorted(skill_proficiencies)

        return armor_proficiencies, weapon_proficiencies, tool_proficiencies, \
               language_proficiencies, skill_proficiencies, other_proficiencies

    def __str__(self):
        ancestry = f'{self.ancestry.name} ({self.subancestry.name})'
        classes = []
        for c_l in self.class_levels.all():
            classes.append(f'{c_l.character_class.name} {c_l.level}')
        classes_str = '/'.join(classes)
        return f'{self.name}: {ancestry} {classes_str}'
