""" Weapon serializers. """
from rest_framework import serializers

from common.serializers import OwnedModelSerializer
from equipment.models import Weapon, WeaponProperty


class WeaponSerializer(OwnedModelSerializer):
    """ Serializer for Weapon model """
    properties = serializers.PrimaryKeyRelatedField(
        queryset=WeaponProperty.objects.all(), many=True)
    class Meta:
        model = Weapon
        fields = '__all__'
        depth = 2
