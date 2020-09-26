""" Serializer base class for when a class has the "owner" and "authorized_editors" attributes. """
from django.contrib.auth import get_user_model
from rest_framework import serializers

from common.models import OwnedModel

class OwnedModelSerializer(serializers.ModelSerializer):
    """ Serializer base for models that subclass OwnedData.
    Protects user data using User Serializer """
    owner = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(), required=False)
    authorized_editors = serializers.PrimaryKeyRelatedField(many=True,
        queryset=get_user_model().objects.all(), required=False)

    class Meta:
        model = OwnedModel
        fields = '__all__'
        abstract = True

    def validate(self, attrs):
        """ Use validate to default owner value to current requester """
        request_user = self.context['request'].user
        if not attrs.get('owner'):
            attrs['owner'] = request_user
        return attrs
