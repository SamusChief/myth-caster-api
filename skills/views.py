""" Skill ViewSets """
from rest_framework import viewsets

from .models import Skill
from .serializers import SkillSerializer


class SkillViewSet(viewsets.ModelViewSet):
    """ ViewSet for ancestry. """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'
