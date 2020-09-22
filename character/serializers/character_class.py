""" CharacterClass serializers. """
from rest_framework import serializers

from common.serializers import OwnedModelSerializer
from character.models import CharacterClass, Archetype, FeaturesAtLevel, \
    SpellsKnownAtLevel, SpellSlotsAtLevel, Feature
from skills.models import Skill


class FeaturesAtLevelSerializer(OwnedModelSerializer):
    """ Serializer for FeaturesAtLevel model """
    features = serializers.PrimaryKeyRelatedField(queryset=Feature.objects.all(), many=True)
    class Meta:
        model = FeaturesAtLevel
        fields = '__all__'
        depth = 1


class SpellsKnownAtLevelSerializer(OwnedModelSerializer):
    """ Serializer for SpellsKnownAtLevel model """
    class Meta:
        model = SpellsKnownAtLevel
        fields = '__all__'
        depth = 1


class SpellSlotsAtLevelSerializer(OwnedModelSerializer):
    """ Serializer for SpellSlotsAtLevel model """
    class Meta:
        model = SpellSlotsAtLevel
        fields = '__all__'
        depth = 1


class CharacterClassSerializer(OwnedModelSerializer):
    """ Serializer for CharacterClass model """
    features = FeaturesAtLevelSerializer(many=True)
    skill_choices = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), many=True)
    spell_slots = SpellSlotsAtLevelSerializer(many=True)
    spells_known = SpellsKnownAtLevelSerializer(many=True)
    class Meta:
        model = CharacterClass
        fields = '__all__'
        depth = 1


class ArchetypeSerializer(CharacterClassSerializer):
    """ Serializer for Archetype model """
    parent = serializers.PrimaryKeyRelatedField(queryset=CharacterClass.objects.all())
    class Meta:
        model = Archetype
        fields = '__all__'
        depth = 1
