from django.db import models


class Ancestry(models.Model):
    """
    Model for representing character ancestry
    TODO
    """
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    features = models.TextField()
