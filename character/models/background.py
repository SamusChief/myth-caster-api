""" Background model. """
from django.db import models

from common.models import OwnedModel, NameStrMixin
from equipment.models import Armor, Tool, Weapon
from skills.models import Skill

from .feature import Feature

class Background(OwnedModel, NameStrMixin):
    """
    Model for representing character background
    TODO

    Attributes:
        name: the name for this background. Should be unique.
        description: text description of the background
        features: features granted to characters by this background
        granted_tools: tools the character gains using this background
        granted_armors: armor proficiencies granted by the background
        granted_weapons: weapon proficiencies granted by the background
        granted_skills: skill proficiency choices granted by the background
        starting_gold: gold that characters with this background start with.
            Can use decimals for silver/copper.
        starting_equipment: The equipment members of this background begin play with.
    """
    name = models.CharField(unique=True, max_length=255, db_index=True)
    description = models.TextField()
    features = models.ManyToManyField(to=Feature)

    granted_tools = models.ManyToManyField(to=Tool)
    granted_armors = models.ManyToManyField(to=Armor)
    granted_weapons = models.ManyToManyField(to=Weapon)
    granted_skills = models.ManyToManyField(to=Skill)
    granted_languages = models.TextField(blank=True, null=True)

    starting_gold = models.FloatField(default=10)
    starting_equipment = models.TextField()
