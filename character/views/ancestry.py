""" Ancestry Viewsets """
from rest_framework import viewsets

from character.models import Ancestry, SubAncestry
from character.serializers import AncestrySerializer, SubAncestrySerializer


class AncestryViewset(viewsets.ModelViewSet):
    """ Viewset for ancestry. """
    queryset = Ancestry.objects.all()
    serializer_class = AncestrySerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'


class SubAncestryViewset(viewsets.ModelViewSet):
    """ Viewset for ancestry. """
    queryset = SubAncestry.objects.all()
    serializer_class = SubAncestrySerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'
