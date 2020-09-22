""" WondrousItem serializers. """
from common.serializers import OwnedModelSerializer
from equipment.models import WondrousItem


class WondrousItemSerializer(OwnedModelSerializer):
    """ Serializer for WondrousItem model """
    class Meta:
        model = WondrousItem
        fields = '__all__'
        depth = 1
