""" Character Viewsets """
from rest_framework import viewsets

from character.models import Character, ClassAndLevel, \
    InventoryAdventuringGear, InventoryArmor, InventoryTool, \
        InventoryWeapon, InventoryWondrousItem, SkillProficiency
from character.serializers import CharacterSerializer, ClassAndLevelSerializer, \
    InventoryAdventuringGearSerializer, InventoryArmorSerializer, \
        InventoryToolSerializer, InventoryWeaponSerializer, InventoryWondrousItemSerializer, \
            SkillProficiencySerializer


class CharacterViewset(viewsets.ModelViewSet):
    """ Viewset for Character. """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'


class ClassAndLevelViewset(viewsets.ModelViewSet):
    """ Viewset for ClassAndLevel. """
    queryset = ClassAndLevel.objects.all()
    serializer_class = ClassAndLevelSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'character_class__name'


class InventoryAdventuringGearViewset(viewsets.ModelViewSet):
    """ Viewset for InventoryAdventuringGear. """
    queryset = InventoryAdventuringGear.objects.all()
    serializer_class = InventoryAdventuringGearSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'gear__name'


class InventoryArmorViewset(viewsets.ModelViewSet):
    """ Viewset for InventoryArmor. """
    queryset = InventoryArmor.objects.all()
    serializer_class = InventoryArmorSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'gear__name'


class InventoryToolViewset(viewsets.ModelViewSet):
    """ Viewset for InventoryTool. """
    queryset = InventoryTool.objects.all()
    serializer_class = InventoryToolSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'gear__name'


class InventoryWeaponViewset(viewsets.ModelViewSet):
    """ Viewset for InventoryWeapon. """
    queryset = InventoryWeapon.objects.all()
    serializer_class = InventoryWeaponSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'gear__name'


class InventoryWondrousItemViewset(viewsets.ModelViewSet):
    """ Viewset for InventoryWondrousItem. """
    queryset = InventoryWondrousItem.objects.all()
    serializer_class = InventoryWondrousItemSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'gear__name'


class SkillProficiencyViewset(viewsets.ModelViewSet):
    """ Viewset for SkillProficiency. """
    queryset = SkillProficiency.objects.all()
    serializer_class = SkillProficiencySerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'skill__name'
