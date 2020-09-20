""" AdventuringGear ViewSets """
from rest_framework import viewsets

from equipment.models import AdventuringGear
from equipment.serializers import AdventuringGearSerializer


class AdventuringGearViewSet(viewsets.ModelViewSet):
    """ ViewSet for AdventuringGear. """
    queryset = AdventuringGear.objects.all()
    serializer_class = AdventuringGearSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'
