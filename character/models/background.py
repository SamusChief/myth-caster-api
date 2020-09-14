""" Background model. """
from django.db import models

from common.models import OwnedModel
from equipment.models import Armor, Tool, Weapon
from skills.models import Skill

class Background(OwnedModel):
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
    """
    name = models.CharField(unique=True, max_length=255, db_index=True)
    description = models.TextField()
    features = models.TextField()

    # TODO add fields for equipment granted, and default skills
    granted_tools = models.ManyToManyField(to=Tool)
    granted_armors = models.ManyToManyField(to=Armor)
    granted_weapons = models.ManyToManyField(to=Weapon)
    granted_skills_default = models.ManyToManyField(to=Skill)
