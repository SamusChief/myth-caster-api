""" Tool ViewSets """
from rest_framework import viewsets

from equipment.models import Tool
from equipment.serializers import ToolSerializer


class ToolViewSet(viewsets.ModelViewSet):
    """ ViewSet for Tool. """
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'
