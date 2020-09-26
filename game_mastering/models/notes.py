""" Model to represent Notes, which are shared with players of a party. """
from django.db import models

from common.models import OwnedModel
from parties.models import Party

from .file import GameMasterFile
from .mixins import PartiesUsersMixin


class Notes(OwnedModel, PartiesUsersMixin):
    """
    Notes model representation. Notes are always hidden from non-gms and non-owners.

    Attributes:
        title: unique indexed name of this handout
        subtitle: an optional, longer, and more descriptive subtitle
        party: the party to these notes are for
        content: the text content of this handout, markdown formatted
        files: uploaded files to be associated with this notes file
    """
    title = models.CharField(unique=True, max_length=255, db_index=True)
    subtitle = models.TextField(blank=True, null=True)
    parties = models.ManyToManyField(to=Party, related_name='party_notes', blank=True)
    content = models.TextField(blank=True, null=True)
    files = models.ManyToManyField(to=GameMasterFile, blank=True, related_name='file_notes')

    def __str__(self):
        return f'Notes: {self.id}|{self.title}'
