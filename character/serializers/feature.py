""" Feature serializers. """
from common.serializers import OwnedModelSerializer
from character.models import Feature


class FeatureSerializer(OwnedModelSerializer):
    """ Serializer for Feature model """
    class Meta:
        model = Feature
        fields = '__all__'
        depth = 1
