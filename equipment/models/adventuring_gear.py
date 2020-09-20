""" Adventuring Gear model. """
from .base_equipment import BaseEquipment


class AdventuringGear(BaseEquipment):
    """ Model for tracking mundane adventuring gear. """

    def __str__(self):
        return 'Adventuring Gear: ' + str(self.name)
