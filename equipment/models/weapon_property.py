from django.db import models


class WeaponProperty(models.Model):
    """
    Model to represent weapon properties.

    Attributes:
        name: the name of the property
        description: a description of what the property does or means mechanically.
            Defaults to null.
    """
    name = models.CharField(unique=True, max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
