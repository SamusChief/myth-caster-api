""" Serializer module for the GameMasterFile model """
from common.serializers import PrivateModelSerializer
from game_mastering.models import GameMasterFile


class GameMasterFileSerializer(PrivateModelSerializer):
    """ Serializer for the GameMasterFile model """
    class Meta:
        model = GameMasterFile
        fields = '__all__'
