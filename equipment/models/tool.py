""" Tool model. """
from .base_equipment import BaseEquipment


class Tool(BaseEquipment):
    """ Model for Tools. """

    def __str__(self):
        return 'Tool: ' + str(self.name)
