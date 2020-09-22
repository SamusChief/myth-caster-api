""" Armor serializers. """
from common.serializers import OwnedModelSerializer
from equipment.models import Armor


class ArmorSerializer(OwnedModelSerializer):
    """ Serializer for Armor model """
    class Meta:
        model = Armor
        fields = '__all__'
        depth = 1
