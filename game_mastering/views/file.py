""" GameMasterFile ViewSets """
from rest_framework import viewsets

from game_mastering.models import GameMasterFile
from game_mastering.serializers import GameMasterFileSerializer


class GameMasterFileViewSet(viewsets.ModelViewSet):
    """ ViewSet for GameMasterFiles. """
    queryset = GameMasterFile.objects.all()
    serializer_class = GameMasterFileSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'title'
