""" Administration ViewSets """
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

from rest_framework import viewsets

from .serializers import UserSerializer, GroupSerializer, PermissionSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """ ViewSet for users. is read only; must use admin panel to modify users """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    search_fields = ['username', 'email']
    filterset_fields = ['username', 'email']
    ordering_fields = ['username', 'email']

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ ViewSet for groups """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'

class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
    """ ViewSet for permissions """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
