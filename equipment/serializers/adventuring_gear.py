""" AdventuringGear serializers. """
from common.serializers import OwnedModelSerializer
from equipment.models import AdventuringGear


class AdventuringGearSerializer(OwnedModelSerializer):
    """ Serializer for AdventuringGear model """
    class Meta:
        model = AdventuringGear
        fields = '__all__'
        depth = 1
