""" Feature serializers. """
from rest_framework import serializers

from character.models import Feature


class FeatureSerializer(serializers.ModelSerializer):
    """ Serializer for Feature model """
    class Meta:
        model = Feature
        fields = '__all__'
