from django.db import models

from .base_equipment import BaseEquipment
from .mixins import MagicItemMixin


class WondrousItem(BaseEquipment, MagicItemMixin):
    """
    Model to represent wondrous items, which usually have some slot associated with them.
    """
    slot = models.CharField(blank=True, null=True, max_length=255)
