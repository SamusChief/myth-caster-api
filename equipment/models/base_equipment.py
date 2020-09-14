""" Abstract model for all Equipment items. """
from django.core import validators
from django.db import models

from common.models import OwnedModel


class BaseEquipment(OwnedModel):
    """
    Abstract class to be used as a mixin for equipment.

    Attributes:
        name: name of the equipment. required, and unique
        description: a description of what the equipment does, looks like, or can be used for.
            Default is null.
        weight: the weight of the item, in pounds.
        cost: the cost of the item, in gold. 1 silver is 0.1, 1 copper is 0.01.
    """
    name = models.CharField(unique=True, max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True)
    weight = models.FloatField(default=0, db_index=True)
    cost = models.IntegerField(default=0, validators=[validators.MinValueValidator(0)], db_index=True)

    class Meta:
        abstract = True
