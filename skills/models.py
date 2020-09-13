""" Skill model. """
from django.db import models

from common.models import OwnedModel


class Skill(OwnedModel):
    """
    Model to represent skills and their unique attributes.

    Attributes:
        name: name of the skill.
        description: description of the skill, possibly including use examples.
    """
    name = models.CharField(unique=True, max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True)
