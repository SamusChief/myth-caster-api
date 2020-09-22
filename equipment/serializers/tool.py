""" Tool serializers. """
from common.serializers import OwnedModelSerializer
from equipment.models import Tool


class ToolSerializer(OwnedModelSerializer):
    """ Serializer for Tool model """
    class Meta:
        model = Tool
        fields = '__all__'
        depth = 1
