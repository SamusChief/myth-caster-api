""" Weapon ViewSets """
import logging

from rest_framework import viewsets

from equipment.models import Weapon, WeaponProperty
from equipment.serializers import WeaponSerializer, WeaponPropertySerializer

logger = logging.getLogger(__name__)


class WeaponViewSet(viewsets.ModelViewSet):
    """ ViewSet for Weapon. """
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'


class WeaponPropertyViewSet(viewsets.ModelViewSet):
    """ ViewSet for WeaponProperty. """
    queryset = WeaponProperty.objects.all()
    serializer_class = WeaponPropertySerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'
