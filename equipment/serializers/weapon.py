""" Weapon serializers. """
from rest_framework import serializers

from equipment.models import Weapon

from .weapon_property import WeaponPropertySerializer

class WeaponSerializer(serializers.ModelSerializer):
    """ Serializer for Weapon model """
    class Meta:
        model = Weapon
        fields = '__all__'

    def to_representation(self, instance):
        """ Serialize Weapons and their properties """
        result = super(WeaponSerializer, self).to_representation(instance)
        properties = instance.properties.all()

        properties_serialized = []
        for prop in properties:
            properties_serialized.append(WeaponPropertySerializer(prop).data)
        result['properties'] = properties_serialized

        return result
