""" Handout ViewSets """
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from game_mastering.filters import HandoutsFilter
from game_mastering.models import Handout
from game_mastering.serializers import HandoutSerializer


class HandoutViewSet(viewsets.ModelViewSet):
    """ ViewSet for Handouts. """
    queryset = Handout.objects.all()
    filter_backends = [
        HandoutsFilter,
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    serializer_class = HandoutSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'title'
