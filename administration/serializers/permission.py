""" Permission serializer implementation. """
from django.contrib.auth.models import Permission, ContentType

from rest_framework import serializers


class ContentTypeSerializer(serializers.ModelSerializer):
    """ Serializer for ContentType model instances """
    class Meta:
        model = ContentType
        fields = ['id', 'name', 'model', 'app_label']


class PermissionSerializer(serializers.ModelSerializer):
    """ Permission model serializer """
    content_type = ContentTypeSerializer(read_only=True)
    class Meta:
        model = Permission
        fields = '__all__'
