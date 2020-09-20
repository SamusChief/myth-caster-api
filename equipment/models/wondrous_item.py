""" Wondrous Item model. """
from django.db import models

from .mixins import MagicItemModel


class WondrousItem(MagicItemModel):
    """
    Model to represent wondrous items, which usually have some slot associated with them.
    """
    slot = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return 'Wondrous Item: ' + str(self.name)
