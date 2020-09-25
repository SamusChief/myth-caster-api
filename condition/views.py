""" Condition ViewSets """
from rest_framework import viewsets

from .models import Condition
from .serializers import ConditionSerializer


class ConditionViewSet(viewsets.ModelViewSet):
    """ ViewSet for Condition. """
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'
