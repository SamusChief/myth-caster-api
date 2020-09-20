""" AdventuringGear serializers. """
from rest_framework import serializers

from equipment.models import AdventuringGear


class AdventuringGearSerializer(serializers.ModelSerializer):
    """ Serializer for AdventuringGear model """
    class Meta:
        model = AdventuringGear
        fields = '__all__'
