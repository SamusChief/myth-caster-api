""" Feature ViewSets """
from rest_framework import viewsets

from character.models import Feature
from character.serializers import FeatureSerializer


class FeatureViewSet(viewsets.ModelViewSet):
    """ ViewSet for Feature. """
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'
