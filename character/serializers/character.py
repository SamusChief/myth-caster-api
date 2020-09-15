""" Character serializers. """
from rest_framework import serializers

from character.models import Character, ClassAndLevel, \
    InventoryAdventuringGear, InventoryArmor, InventoryTool, \
        InventoryWeapon, InventoryWondrousItem, SkillProficiency


class CharacterSerializer(serializers.ModelSerializer):
    """ Serializer for Character model """
    class Meta:
        model = Character
        fields = '__all__'


class ClassAndLevelSerializer(serializers.ModelSerializer):
    """ Serializer for ClassAndLevel model """
    class Meta:
        model = ClassAndLevel
        fields = '__all__'


class InventoryAdventuringGearSerializer(serializers.ModelSerializer):
    """ Serializer for InventoryAdventuringGear model """
    class Meta:
        model = InventoryAdventuringGear
        fields = '__all__'


class InventoryArmorSerializer(serializers.ModelSerializer):
    """ Serializer for InventoryArmor model """
    class Meta:
        model = InventoryArmor
        fields = '__all__'


class InventoryToolSerializer(serializers.ModelSerializer):
    """ Serializer for InventoryTool model """
    class Meta:
        model = InventoryTool
        fields = '__all__'


class InventoryWeaponSerializer(serializers.ModelSerializer):
    """ Serializer for InventoryWeapon model """
    class Meta:
        model = InventoryWeapon
        fields = '__all__'


class InventoryWondrousItemSerializer(serializers.ModelSerializer):
    """ Serializer for InventoryWondrousItem model """
    class Meta:
        model = InventoryWondrousItem
        fields = '__all__'


class SkillProficiencySerializer(serializers.ModelSerializer):
    """ Serializer for SkillProficiency model """
    class Meta:
        model = SkillProficiency
        fields = '__all__'
