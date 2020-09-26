""" Notes ViewSets """
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from game_mastering.filters import NotesFilter
from game_mastering.models import Notes
from game_mastering.serializers import NotesSerializer


class NotesViewSet(viewsets.ModelViewSet):
    """ ViewSet for Notes. """
    queryset = Notes.objects.all()
    filter_backends = [
        NotesFilter,
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    serializer_class = NotesSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'title'
