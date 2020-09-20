""" Tool serializers. """
from rest_framework import serializers

from equipment.models import Tool


class ToolSerializer(serializers.ModelSerializer):
    """ Serializer for Tool model """
    class Meta:
        model = Tool
        fields = '__all__'