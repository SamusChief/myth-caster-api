""" Party Serializer """
from django.contrib.auth import get_user_model

from rest_framework import serializers

from common.serializers import OwnedModelSerializer
from .models import Party

class PartySerializer(OwnedModelSerializer):
    """ Serializer for Party instances. Protects user data. """
    game_masters = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(), many=True)
    players = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(), many=True)
    class Meta:
        model = Party
        fields = '__all__'
        depth = 1

    def validate(self, attrs):
        """ Use validate to default game_masters list value to current requester """
        attrs = super(PartySerializer, self).validate(attrs)
        request_user = self.context['request'].user
        if not attrs.get('game_masters'):
            attrs['game_masters'] = [request_user]
        return attrs
