""" Background serializers. """
from rest_framework import serializers

from character.models import Background


class BackgroundSerializer(serializers.ModelSerializer):
    """ Serializer for Background model """
    class Meta:
        model = Background
        fields = '__all__'
