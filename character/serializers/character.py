""" Character serializers. """
from rest_framework import serializers

from common.serializers import OwnedModelSerializer
from character.models import Character, ClassAndLevel, \
    InventoryAdventuringGear, InventoryArmor, InventoryTool, \
        InventoryWeapon, InventoryWondrousItem, SkillProficiency, \
            Ancestry, SubAncestry, Background


class ClassAndLevelSerializer(OwnedModelSerializer):
    """ Serializer for ClassAndLevel model """
    class Meta:
        model = ClassAndLevel
        fields = '__all__'
        depth = 1


class InventoryAdventuringGearSerializer(OwnedModelSerializer):
    """ Serializer for InventoryAdventuringGear model """
    class Meta:
        model = InventoryAdventuringGear
        fields = '__all__'
        depth = 1


class InventoryArmorSerializer(OwnedModelSerializer):
    """ Serializer for InventoryArmor model """
    class Meta:
        model = InventoryArmor
        fields = '__all__'
        depth = 1


class InventoryToolSerializer(OwnedModelSerializer):
    """ Serializer for InventoryTool model """
    class Meta:
        model = InventoryTool
        fields = '__all__'
        depth = 1


class InventoryWeaponSerializer(OwnedModelSerializer):
    """ Serializer for InventoryWeapon model """
    class Meta:
        model = InventoryWeapon
        fields = '__all__'
        depth = 1


class InventoryWondrousItemSerializer(OwnedModelSerializer):
    """ Serializer for InventoryWondrousItem model """
    class Meta:
        model = InventoryWondrousItem
        fields = '__all__'
        depth = 1


class SkillProficiencySerializer(OwnedModelSerializer):
    """ Serializer for SkillProficiency model """
    class Meta:
        model = SkillProficiency
        fields = '__all__'
        depth = 1



class CharacterSerializer(OwnedModelSerializer):
    """ Serializer for Character model """
    # Fields must be chosen, not created on a character
    background = serializers.PrimaryKeyRelatedField(queryset=Background.objects.all())
    ancestry = serializers.PrimaryKeyRelatedField(queryset=Ancestry.objects.all())
    subancestry = serializers.PrimaryKeyRelatedField(queryset=SubAncestry.objects.all())

    # These fields can be created on a character
    class_levels = ClassAndLevelSerializer(many=True)
    skills = SkillProficiencySerializer(many=True)
    inventory_adventuring_gear = InventoryAdventuringGearSerializer(many=True)
    inventory_armors = InventoryArmorSerializer(many=True)
    inventory_tools = InventoryToolSerializer(many=True)
    inventory_weapons = InventoryWeaponSerializer(many=True)
    inventory_wondrous_items = InventoryWondrousItemSerializer(many=True)
    class Meta:
        model = Character
        fields = '__all__'
        depth = 1
