""" CharacterClass ViewSets """
from rest_framework import viewsets

from character.models import CharacterClass, Archetype, \
    FeaturesAtLevel, SpellsKnownAtLevel, SpellSlotsAtLevel
from character.serializers import CharacterClassSerializer, ArchetypeSerializer, \
    FeaturesAtLevelSerializer, SpellsKnownAtLevelSerializer, SpellSlotsAtLevelSerializer


class CharacterClassViewSet(viewsets.ModelViewSet):
    """ ViewSet for CharacterClass. """
    queryset = CharacterClass.objects.all()
    serializer_class = CharacterClassSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'


class ArchetypeViewSet(viewsets.ModelViewSet):
    """ ViewSet for Archetype. """
    queryset = Archetype.objects.all()
    serializer_class = ArchetypeSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'


class FeaturesAtLevelViewSet(viewsets.ModelViewSet):
    """ ViewSet for FeaturesAtLevel. """
    queryset = FeaturesAtLevel.objects.all()
    serializer_class = FeaturesAtLevelSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'level'


class SpellsKnownAtLevelViewSet(viewsets.ModelViewSet):
    """ ViewSet for SpellsKnownAtLevel. """
    queryset = SpellsKnownAtLevel.objects.all()
    serializer_class = SpellsKnownAtLevelSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'level'


class SpellSlotsAtLevelViewSet(viewsets.ModelViewSet):
    """ ViewSet for SpellSlotsAtLevel. """
    queryset = SpellSlotsAtLevel.objects.all()
    serializer_class = SpellSlotsAtLevelSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'level'
