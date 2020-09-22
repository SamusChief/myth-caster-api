""" Skill serializers. """
from common.serializers import OwnedModelSerializer
from .models import Skill


class SkillSerializer(OwnedModelSerializer):
    """ Serializer for Skill model """
    class Meta:
        model = Skill
        fields = '__all__'
        depth = 1
