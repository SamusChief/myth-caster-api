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
        description: 
    """
    name = models.CharField(unique=True)
    description = models.TextField()
    features = models.TextField()

    # TODO add fields for equipment granted, and default skills
    granted_tools = models.ManyToManyField(to=Tool, blank=True, null=True)
    granted_armors = models.ManyToManyField(to=Tool, blank=True, null=True)
    granted_weapons = models.ManyToManyField(to=Tool, blank=True, null=True)
    granted_skills_default = models.ManyToManyField(to=Skill, blank=True, null=True)
