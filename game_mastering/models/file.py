""" Model for tracking file uploads to the server """
from django.db import models

from common.models import PrivateModel


class GameMasterFile(PrivateModel):
    """
    Model to represent specific files.

    Attributes
        upload: the file uploaded to the server
    """
    name = models.CharField(unique=True, max_length=255, db_index=True)
    upload = models.FileField(upload_to='game_master_materials/%Y/%m/%d/')

    def __str__(self):
        return f'File: {self.id}|{self.name}'
