""" Admin panel regitsrtion for character app """
from django.contrib import admin

from .models import Ancestry, SubAncestry, Background, Character, ClassAndLevel, \
    InventoryAdventuringGear, InventoryArmor, InventoryTool, InventoryWeapon, \
        InventoryWondrousItem, CharacterClass, Archetype, FeaturesAtLevel, \
            SpellsKnownAtLevel, SpellSlotsAtLevel, Feature

# Register your models here.
admin.site.register(Feature)
admin.site.register([Ancestry, SubAncestry])
admin.site.register(Background)
admin.site.register([
    Character,
    ClassAndLevel,
    InventoryAdventuringGear,
    InventoryArmor,
    InventoryTool,
    InventoryWeapon,
    InventoryWondrousItem
])
admin.site.register([
    CharacterClass,
    Archetype,
    FeaturesAtLevel,
    SpellsKnownAtLevel,
    SpellSlotsAtLevel
])
