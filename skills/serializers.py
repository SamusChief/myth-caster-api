""" Skill serializers. """
from rest_framework import serializers

from .models import Skill


class SkillSerializer(serializers.ModelSerializer):
    """ Serializer for Skill model """
    class Meta:
        model = Skill
        fields = '__all__'
