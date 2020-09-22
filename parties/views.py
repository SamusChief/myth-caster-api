""" Party ViewSets """
from rest_framework import viewsets

from .models import Party
from .serializers import PartySerializer


class PartyViewSet(viewsets.ModelViewSet):
    """ ViewSet for Party. """
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'
