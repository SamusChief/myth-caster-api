""" Character ViewSets """
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from character.models import Character, ClassAndLevel, \
    InventoryAdventuringGear, InventoryArmor, InventoryTool, \
        InventoryWeapon, InventoryWondrousItem, SkillProficiency
from character.serializers import CharacterSerializer, ClassAndLevelSerializer, \
    InventoryAdventuringGearSerializer, InventoryArmorSerializer, \
        InventoryToolSerializer, InventoryWeaponSerializer, InventoryWondrousItemSerializer, \
            SkillProficiencySerializer
from character.filters import CharacterOwnedOrAdminFilter


class CharacterViewSet(viewsets.ModelViewSet):
    """ ViewSet for Character. """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
        CharacterOwnedOrAdminFilter
    ]
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'


class ClassAndLevelViewSet(viewsets.ModelViewSet):
    """ ViewSet for ClassAndLevel. """
    queryset = ClassAndLevel.objects.all()
    serializer_class = ClassAndLevelSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'character_class__name'


class InventoryAdventuringGearViewSet(viewsets.ModelViewSet):
    """ ViewSet for InventoryAdventuringGear. """
    queryset = InventoryAdventuringGear.objects.all()
    serializer_class = InventoryAdventuringGearSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'gear__name'


class InventoryArmorViewSet(viewsets.ModelViewSet):
    """ ViewSet for InventoryArmor. """
    queryset = InventoryArmor.objects.all()
    serializer_class = InventoryArmorSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'gear__name'


class InventoryToolViewSet(viewsets.ModelViewSet):
    """ ViewSet for InventoryTool. """
    queryset = InventoryTool.objects.all()
    serializer_class = InventoryToolSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'gear__name'


class InventoryWeaponViewSet(viewsets.ModelViewSet):
    """ ViewSet for InventoryWeapon. """
    queryset = InventoryWeapon.objects.all()
    serializer_class = InventoryWeaponSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'gear__name'


class InventoryWondrousItemViewSet(viewsets.ModelViewSet):
    """ ViewSet for InventoryWondrousItem. """
    queryset = InventoryWondrousItem.objects.all()
    serializer_class = InventoryWondrousItemSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'gear__name'


class SkillProficiencyViewSet(viewsets.ModelViewSet):
    """ ViewSet for SkillProficiency. """
    queryset = SkillProficiency.objects.all()
    serializer_class = SkillProficiencySerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'skill__name'
