""" Ancestry serializers. """
from rest_framework import serializers

from character.models import Ancestry, SubAncestry


class AncestrySerializer(serializers.ModelSerializer):
    """ Serializer for Ancestry model """
    class Meta:
        model = Ancestry
        fields = '__all__'


class SubAncestrySerializer(serializers.ModelSerializer):
    """ Serializer for SubAncestry model """
    class Meta:
        model = SubAncestry
        fields = '__all__'
