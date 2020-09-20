""" WondrousItem serializers. """
from rest_framework import serializers

from equipment.models import WondrousItem


class WondrousItemSerializer(serializers.ModelSerializer):
    """ Serializer for WondrousItem model """
    class Meta:
        model = WondrousItem
        fields = '__all__'
