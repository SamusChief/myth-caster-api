""" Serializers for Conditions """
from common.serializers import OwnedModelSerializer

from .models import Condition


class ConditionSerializer(OwnedModelSerializer):
    """ Serializer for the Condition model """
    class Meta:
        model = Condition
        fields = '__all__'
        depth = 1
