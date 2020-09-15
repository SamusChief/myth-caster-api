""" Ancestry model. """
from django.db import models

from common.models import OwnedModel, NameStrMixin

from .feature import Feature


class Ancestry(OwnedModel, NameStrMixin):
    """
    Model for representing character ancestry, referred to in the SRD rules as "race"

    Attributes:
        name: the unique name of the ancestry
        description: a general physical description of members of this ancestry.
        features: features granted to members of this ancestry
    """
    name = models.CharField(unique=True, max_length=255, db_index=True)
    description = models.TextField()
    features = models.ManyToManyField(to=Feature)


class SubAncestry(Ancestry):
    """
    Model for tracking sub ancestries.
    In addition to Ancestry fields, there is a parent field as well.
    """
    parent = models.ForeignKey(to=Ancestry, on_delete=models.CASCADE, related_name='child')

    def __str__(self):
        return f'{self.parent.name}: {self.name}'
