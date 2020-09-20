""" Armor ViewSets """
from rest_framework import viewsets

from equipment.models import Armor
from equipment.serializers import ArmorSerializer


class ArmorViewSet(viewsets.ModelViewSet):
    """ ViewSet for Armor. """
    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'
