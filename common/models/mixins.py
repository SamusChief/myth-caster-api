""" Model mixins for the app to use. """
from django.contrib.auth import get_user_model
from django.db import models


class OwnedModel(models.Model):
    """ Abstract model for owned data. Used to help permissions scanning """
    owner = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL, blank=True, null=True)
    authorized_editors = models.ManyToManyField(
        to=get_user_model(),
        related_name='+',
        blank=True
    )

    class Meta:
        abstract = True
