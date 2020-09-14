""" User serializer implementation. Protects sensitive fields. """
from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """ User model serializer to protect sensitive data """
    class Meta:
        model = User
        fields = ['username', 'email']
