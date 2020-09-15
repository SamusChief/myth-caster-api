""" Model mixins for the app to use. """
from django.contrib.auth import get_user_model
from django.db import models

class OwnedModel(models.Model):
    """ Abstract model for owned data. Used to help permissions scanning """
    owner = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL, blank=True, null=True)
    authorized_editors = models.ManyToManyField(
        to=get_user_model(),
        related_name='+'
    )

    class Meta:
        abstract = True

class NameStrMixin:
    """ Mixin to give a model a __str__ implementation based on name field. """
    def __str__(self):
        return getattr(self, 'name', 'No Name Field')
