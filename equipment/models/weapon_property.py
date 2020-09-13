from django.db import models


class WeaponProperty(models.Model):
    """
    Model to represent weapon properties.

    Attributes:
        name: the name of the property
        description: a description of what the property does or means mechanically.
            Defaults to null.
    """
    name = models.CharField(unique=True)
    description = models.TextField(blank=True, null=True)
