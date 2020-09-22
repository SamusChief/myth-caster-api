""" Ancestry serializers. """
from rest_framework import serializers

from common.serializers import OwnedModelSerializer
from character.models import Ancestry, SubAncestry, Feature


class AncestrySerializer(OwnedModelSerializer):
    """ Serializer for Ancestry model """
    features = serializers.PrimaryKeyRelatedField(queryset=Feature.objects.all(), many=True)
    class Meta:
        model = Ancestry
        fields = '__all__'
        depth = 1


class SubAncestrySerializer(AncestrySerializer):
    """ Serializer for SubAncestry model """
    parent = serializers.PrimaryKeyRelatedField(queryset=Ancestry.objects.all())
    class Meta:
        model = SubAncestry
        fields = '__all__'
        depth = 1
