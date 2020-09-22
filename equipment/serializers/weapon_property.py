""" WeaponProperty serializers. """
from common.serializers import OwnedModelSerializer
from equipment.models import WeaponProperty


class WeaponPropertySerializer(OwnedModelSerializer):
    """ Serializer for WeaponProperty model """
    class Meta:
        model = WeaponProperty
        fields = '__all__'
        depth = 1
