""" Spell ViewSets """
from rest_framework import viewsets

from .models import Spell
from .serializers import SpellSerializer


class SpellViewSet(viewsets.ModelViewSet):
    """ ViewSet for Spells. """
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'
