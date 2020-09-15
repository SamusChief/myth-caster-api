""" CharacterClass Viewsets """
from rest_framework import viewsets

from character.models import CharacterClass, Archetype, \
    FeaturesAtLevel, SpellsKnownAtLevel, SpellSlotsAtLevel
from character.serializers import CharacterClassSerializer, ArchetypeSerializer, \
    FeaturesAtLevelSerializer, SpellsKnownAtLevelSerializer, SpellSlotsAtLevelSerializer


class CharacterClassViewset(viewsets.ModelViewSet):
    """ Viewset for CharacterClass. """
    queryset = CharacterClass.objects.all()
    serializer_class = CharacterClassSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'


class ArchetypeViewset(viewsets.ModelViewSet):
    """ Viewset for Archetype. """
    queryset = Archetype.objects.all()
    serializer_class = ArchetypeSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'


class FeaturesAtLevelViewset(viewsets.ModelViewSet):
    """ Viewset for FeaturesAtLevel. """
    queryset = FeaturesAtLevel.objects.all()
    serializer_class = FeaturesAtLevelSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'level'


class SpellsKnownAtLevelViewset(viewsets.ModelViewSet):
    """ Viewset for SpellsKnownAtLevel. """
    queryset = SpellsKnownAtLevel.objects.all()
    serializer_class = SpellsKnownAtLevelSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'level'


class SpellSlotsAtLevelViewset(viewsets.ModelViewSet):
    """ Viewset for SpellSlotsAtLevel. """
    queryset = SpellSlotsAtLevel.objects.all()
    serializer_class = SpellSlotsAtLevelSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'level'
