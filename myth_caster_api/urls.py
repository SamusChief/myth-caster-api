"""myth_caster_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_framework_nested import routers

from administration.views import UserViewSet, GroupViewSet, PermissionViewSet
from character.views import AncestryViewSet, BackgroundViewSet, CharacterClassViewSet, \
    CharacterViewSet, FeatureViewSet, SubAncestryViewSet, ArchetypeViewSet
from equipment.views import AdventuringGearViewSet, ArmorViewSet, ToolViewSet, \
    WeaponViewSet, WondrousItemViewSet, WeaponPropertyViewSet
from skills.views import SkillViewSet
from spells.views import SpellViewSet
from parties.views import PartyViewSet
from condition.views import ConditionViewSet

router = routers.DefaultRouter()
# Admin Routes
router.register(r'api/users', UserViewSet, basename='user-readonly-viewset')
router.register(r'api/groups', GroupViewSet, basename='group-readonly-viewset')
router.register(r'api/permissions', PermissionViewSet, basename='permission-readonly-viewset')

# Character Routes
router.register(r'api/characters', CharacterViewSet)
router.register(r'api/ancestries/subancestries', SubAncestryViewSet)
router.register(r'api/ancestries', AncestryViewSet)
router.register(r'api/backgrounds', BackgroundViewSet)
router.register(r'api/classes/archetypes', ArchetypeViewSet)
router.register(r'api/classes', CharacterClassViewSet)
router.register(r'api/features', FeatureViewSet)

# Equipment Routes
router.register(r'api/equipment/adventuring_gear', AdventuringGearViewSet)
router.register(r'api/equipment/armor', ArmorViewSet)
router.register(r'api/equipment/tools', ToolViewSet)
router.register(r'api/equipment/weapons/properties', WeaponPropertyViewSet)
router.register(r'api/equipment/weapons', WeaponViewSet)
router.register(r'api/equipment/wondrous_items', WondrousItemViewSet)

# Skills routes
router.register(r'api/skills', SkillViewSet)

# Spells routes
router.register(r'api/spells', SpellViewSet)

# Parties routes
router.register(r'api/parties', PartyViewSet)

# Conditions routes
router.register(r'api/conditions', ConditionViewSet)

urlpatterns = [
    path('api/django/', admin.site.urls),
]
urlpatterns += router.urls
