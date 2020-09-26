""" Serializer module for the Notes model """
from common.serializers import OwnedModelSerializer
from game_mastering.models import Notes
from game_mastering.serializers import GameMasterFileSerializer


class NotesSerializer(OwnedModelSerializer):
    """ Serializer for the Notes model. Includes secret content. """
    files = GameMasterFileSerializer(many=True, required=False)
    class Meta:
        model = Notes
        fields = '__all__'
