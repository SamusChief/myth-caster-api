""" CharacterClass serializers. """
from rest_framework import serializers

from character.models import CharacterClass, Archetype, FeaturesAtLevel, \
    SpellsKnownAtLevel, SpellSlotsAtLevel


class CharacterClassSerializer(serializers.ModelSerializer):
    """ Serializer for CharacterClass model """
    class Meta:
        model = CharacterClass
        fields = '__all__'


class ArchetypeSerializer(serializers.ModelSerializer):
    """ Serializer for Archetype model """
    class Meta:
        model = Archetype
        fields = '__all__'


class FeaturesAtLevelSerializer(serializers.ModelSerializer):
    """ Serializer for FeaturesAtLevel model """
    class Meta:
        model = FeaturesAtLevel
        fields = '__all__'


class SpellsKnownAtLevelSerializer(serializers.ModelSerializer):
    """ Serializer for SpellsKnownAtLevel model """
    class Meta:
        model = SpellsKnownAtLevel
        fields = '__all__'


class SpellSlotsAtLevelSerializer(serializers.ModelSerializer):
    """ Serializer for SpellSlotsAtLevel model """
    class Meta:
        model = SpellSlotsAtLevel
        fields = '__all__'
