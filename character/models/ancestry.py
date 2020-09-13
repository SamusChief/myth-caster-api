from django.db import models


class Ancestry(models.Model):
    """
    Model for representing character ancestry
    TODO
    """
    name = models.CharField()
    description = models.TextField()
    features = models.TextField()
