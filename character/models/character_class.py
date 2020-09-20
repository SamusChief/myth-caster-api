""" Models for representing Character Class and archetypes """
from django.db import models

from common.models import OwnedModel
from skills.models import Skill

from .feature import Feature

STRENGTH = 'STR'
DEXTERITY = 'DEX'
CONSTITUTION = 'CON'
INTELLIGENCE = 'INT'
WISDOM = 'WIS'
CHARISMA = 'CHA'
SAVING_THROW_MAJOR = [
    (DEXTERITY, 'dexterity'),
    (CONSTITUTION, 'constitution'),
    (WISDOM, 'wisdom')
]
SAVING_THROW_MINOR = [
    (STRENGTH, 'strength'),
    (INTELLIGENCE, 'intelligence'),
    (CHARISMA, 'charisma')
]

D4 = '4'
D6 = '6'
D8 = '8'
D10 = '10'
D12 = '12'
D20 = '20'
HIT_DIE_CHOICES = [
    (D4, 'd4'),
    (D6, 'd6'),
    (D8, 'd8'),
    (D10, 'd10'),
    (D12, 'd12'),
    (D20, 'd20')
]


class FeaturesAtLevel(OwnedModel):
    """
    Model to represent features granted by a class at a certain level.

    Attributes:
        character_level: the level for this entry
        features: the features acquired at this level
    """
    character_level = models.PositiveIntegerField(db_index=True)
    features = models.ManyToManyField(to=Feature)


class SpellSlotsAtLevel(OwnedModel):
    """
    Model to represent how many spell slots a class gets at a certain level

    Attributes:
        character_level: the level for this entry
        level_1: spell slots at this level
        level_2: spell slots at this level
        level_3: spell slots at this level
        level_4: spell slots at this level
        level_5: spell slots at this level
        level_6: spell slots at this level
        level_7: spell slots at this level
        level_8: spell slots at this level
        level_9: spell slots at this level
    """
    character_level = models.PositiveIntegerField(db_index=True)
    level_1 = models.PositiveIntegerField(default=0)
    level_2 = models.PositiveIntegerField(default=0)
    level_3 = models.PositiveIntegerField(default=0)
    level_4 = models.PositiveIntegerField(default=0)
    level_5 = models.PositiveIntegerField(default=0)
    level_6 = models.PositiveIntegerField(default=0)
    level_7 = models.PositiveIntegerField(default=0)
    level_8 = models.PositiveIntegerField(default=0)
    level_9 = models.PositiveIntegerField(default=0)


class SpellsKnownAtLevel(SpellSlotsAtLevel):
    """
    Model to represent how many spell slots a class gets at a certain level.
    Derived from SpellSlotsAtLevel, but also tracks Level 0 spells.

    Attributes:
        level_0: cantrip spells known at this level
    """
    level_0 = models.PositiveIntegerField(default=0)


class CharacterClass(OwnedModel):
    """
    Model to represent classes and their attributes

    Attributes:
        name: Unique name of the class
        description: a description of the class to help players understand its context
        skill_choices: the skills this class has domain over.
        skill_number: the number of skills a character chooses at 1st level
        multiclass_skill_number: the number of skills a character chooses
            if they dip into this class.
        equipment_choices: the options a character of 1st levle has for starting equipment.
        major_saving_throw: which of the 3 most rolled saves the class is proficient in
        minor_saving_throw: which of the 3 less rolled saves the class is proficient in
        proficient_light_armor: whether this class can use light armor effectively
        proficient_heavy_armor: whether this class can use heavy armor effectively
        proficient_martial_weapons: whether this class can use martial weapons effectively
        proficient_simple_weapons: whether this class can use simple weapons effectively
        proficient_other: special/other proficiencies granted to this class
        features: mapping to features granted by level
        spell_slots: mapping to model showing spell slots by character level
        spells_known: mapping to model showing spells known by character level
    """
    name = models.CharField(unique=True, max_length=255, db_index=True)
    hit_die = models.CharField(choices=HIT_DIE_CHOICES, max_length=2)
    description = models.TextField()

    # Proficiencies
    skill_choices = models.ManyToManyField(to=Skill)
    skill_number = models.PositiveIntegerField(default=0)
    multiclass_skill_number = models.PositiveIntegerField(default=0)
    equipment_choices = models.TextField()
    major_saving_throw = models.CharField(choices=SAVING_THROW_MAJOR, max_length=3)
    minor_saving_throw = models.CharField(choices=SAVING_THROW_MINOR, max_length=3)
    proficient_light_armor = models.BooleanField(default=False)
    proficient_heavy_armor = models.BooleanField(default=False)
    proficient_shields = models.BooleanField(default=False)
    proficient_martial_weapons = models.BooleanField(default=False)
    proficient_simple_weapons = models.BooleanField(default=False)
    proficient_other = models.TextField(blank=True, null=True)

    # Stuff by level
    features = models.ManyToManyField(to=FeaturesAtLevel,
                                      related_name='character_class_with_feature')
    spell_slots = models.ManyToManyField(to=SpellSlotsAtLevel,
                                         related_name='character_class_with_spell_slots')
    spells_known = models.ManyToManyField(to=SpellsKnownAtLevel,
                                          related_name='character_class_with_spells_known')

    def __str__(self):
        return str(self.name)


class Archetype(CharacterClass):
    """
    Model to represent archetypes of classes.

    Attributes:
        parent: the parent class of this archetype
    """
    parent = models.ForeignKey(to=CharacterClass, on_delete=models.CASCADE, related_name='child')

    def __str__(self):
        return f'{self.parent.name}: {self.name}'
