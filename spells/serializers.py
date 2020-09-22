""" Spell serializers. """
from rest_framework import serializers

from common.serializers import OwnedModelSerializer
from character.models import CharacterClass

from .models import Spell


class SpellSerializer(OwnedModelSerializer):
    """ Serializer for Spell model """
    character_classes = serializers.PrimaryKeyRelatedField(
        queryset=CharacterClass.objects.all(), many=True)
    class Meta:
        model = Spell
        fields = '__all__'
        depth = 1
