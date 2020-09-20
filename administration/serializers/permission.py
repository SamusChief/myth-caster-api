""" Permission serializer implementation. """
from django.contrib.auth.models import Permission

from rest_framework import serializers


class PermissionSerializer(serializers.ModelSerializer):
    """ Permission model serializer """
    class Meta:
        model = Permission
        fields = '__all__'

    def to_representation(self, instance):
        """ Override in order to serialize content_type field as well """
        result = super(PermissionSerializer, self).to_representation(instance)
        if result.get('content_type', None):
            result['content_type'] = {
                'id': getattr(instance.content_type, 'id'),
                'name': getattr(instance.content_type, 'name'),
                'model': getattr(instance.content_type, 'model'),
                'app_label': getattr(instance.content_type, 'app_label')
            }
        return result
