""" WondrousItem ViewSets """
from rest_framework import viewsets

from equipment.models import WondrousItem
from equipment.serializers import WondrousItemSerializer


class WondrousItemViewSet(viewsets.ModelViewSet):
    """ ViewSet for WondrousItem. """
    queryset = WondrousItem.objects.all()
    serializer_class = WondrousItemSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'
