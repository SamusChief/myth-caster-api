""" Armor serializers. """
from rest_framework import serializers

from equipment.models import Armor


class ArmorSerializer(serializers.ModelSerializer):
    """ Serializer for Armor model """
    class Meta:
        model = Armor
        fields = '__all__'
