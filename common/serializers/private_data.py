""" Serializer base class for when a class has the "is_private" attributes. """
from common.models import PrivateModel

from .owned_data import OwnedModelSerializer


class PrivateModelSerializer(OwnedModelSerializer):
    """ Serializer base for models that subclass PrivateModel. """

    class Meta:
        model = PrivateModel
        fields = '__all__'
        abstract = True
