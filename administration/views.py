""" Administration Viewsets """
from django.contrib.auth import get_user_model

from rest_framework import viewsets

from .serializers import UserSerializer


class UserViewset(viewsets.ReadOnlyModelViewSet):
    """ Viewset for users. is read only; must use admin panel to modify users """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    search_fields = ['username', 'email']
    filterset_fields = ['username', 'email']
    ordering_fields = ['username', 'email']
