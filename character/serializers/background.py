""" Background serializers. """
from rest_framework import serializers

from common.serializers import OwnedModelSerializer
from character.models import Background, Feature
from skills.models import Skill
from equipment.models import Armor, Tool, Weapon


class BackgroundSerializer(OwnedModelSerializer):
    """ Serializer for Background model """
    features = serializers.PrimaryKeyRelatedField(queryset=Feature.objects.all(), many=True)
    suggested_armors = serializers.PrimaryKeyRelatedField(queryset=Armor.objects.all(), many=True)
    suggested_weapons = serializers.PrimaryKeyRelatedField(queryset=Weapon.objects.all(), many=True)
    suggested_tools = serializers.PrimaryKeyRelatedField(queryset=Tool.objects.all(), many=True)
    suggested_skills = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), many=True)
    class Meta:
        model = Background
        fields = '__all__'
        depth = 1
