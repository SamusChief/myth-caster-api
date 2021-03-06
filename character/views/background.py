""" Background ViewSets """
from rest_framework import viewsets

from character.models import Background
from character.serializers import BackgroundSerializer


class BackgroundViewSet(viewsets.ModelViewSet):
    """ ViewSet for Background. """
    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'
