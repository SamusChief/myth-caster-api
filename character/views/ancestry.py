""" Ancestry ViewSets """
from rest_framework import viewsets

from character.models import Ancestry, SubAncestry
from character.serializers import AncestrySerializer, SubAncestrySerializer


class AncestryViewSet(viewsets.ModelViewSet):
    """ ViewSet for ancestry. """
    queryset = Ancestry.objects.all()
    serializer_class = AncestrySerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'


class SubAncestryViewSet(viewsets.ModelViewSet):
    """ ViewSet for ancestry. """
    queryset = SubAncestry.objects.all()
    serializer_class = SubAncestrySerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'
