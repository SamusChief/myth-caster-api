""" Models for Conditions app """
from django.db import models

from common.models import OwnedModel


class Condition(OwnedModel):
    """ Condition model """
    name = models.CharField(unique=True, max_length=255, db_index=True)
    description = models.TextField()

    def __str__(self):
        return f'Condition: {self.name}'
