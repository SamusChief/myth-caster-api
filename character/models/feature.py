""" Background model. """
from django.db import models

from common.models import OwnedModel


class Feature(OwnedModel):
    """
    Model for representing features

    Attributes:
        name: the name for this feature. Should be unique.
        description: text description of the feature, typically describing its uses
        prerequisite_strength: required strength score value. Defaults to 0 (No requirement)
        prerequisite_dexterity: required dexterity score value. Defaults to 0 (No requirement)
        prerequisite_constitution: required constitution score value. Defaults to 0 (No requirement)
        prerequisite_intelligence: required intelligence score value. Defaults to 0 (No requirement)
        prerequisite_wisdom: required wisdom score value. Defaults to 0 (No requirement)
        prerequisite_charisma: required charisma score value. Defaults to 0 (No requirement)
    """
    name = models.CharField(unique=True, max_length=255, db_index=True)
    description = models.TextField()

    # Ability feature prerequisite fields
    prerequisite_strength = models.IntegerField(default=0, db_index=True)
    prerequisite_dexterity = models.IntegerField(default=0, db_index=True)
    prerequisite_constitution = models.IntegerField(default=0, db_index=True)
    prerequisite_intelligence = models.IntegerField(default=0, db_index=True)
    prerequisite_wisdom = models.IntegerField(default=0, db_index=True)
    prerequisite_charisma = models.IntegerField(default=0, db_index=True)

    def __str__(self):
        return str(self.name)
