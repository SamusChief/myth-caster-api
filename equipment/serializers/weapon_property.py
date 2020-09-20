""" WeaponProperty serializers. """
from rest_framework import serializers

from equipment.models import WeaponProperty


class WeaponPropertySerializer(serializers.ModelSerializer):
    """ Serializer for WeaponProperty model """
    class Meta:
        model = WeaponProperty
        fields = '__all__'
