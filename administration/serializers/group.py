""" Group serializer implementation. """
from django.contrib.auth.models import Group

from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    """ Group model serializer """
    class Meta:
        model = Group
        fields = '__all__'
