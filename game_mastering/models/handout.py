""" Model to represent Handouts, which are shared with players of a party. """
from django.db import models

from common.models import OwnedModel
from parties.models import Party

from .file import GameMasterFile
from .mixins import PartiesUsersMixin


class Handout(OwnedModel, PartiesUsersMixin):
    """
    Handout model representation.

    Attributes:
        title: unique indexed name of this handout
        subtitle: an optional, longer, and more descriptive subtitle
        parties: the parties to share this handout with
        content: the text content of this handout, markdown formatted
        secret_content: content that is only visible to game masters, markdown formatted
        files: files uploaded to associated with this Handout.
            If a file is toggled to be private, players in the party will not be able to
            view it, but they will be able to view the normal public content.
    """
    title = models.CharField(unique=True, max_length=255, db_index=True)
    subtitle = models.TextField(blank=True, null=True)
    parties = models.ManyToManyField(to=Party, related_name='party_handouts', blank=True)
    content = models.TextField(blank=True, null=True)
    secret_content = models.TextField(blank=True, null=True)
    files = models.ManyToManyField(to=GameMasterFile, blank=True, related_name='file_handouts')

    def __str__(self):
        return f'Handout: {self.id}|{self.title}'
