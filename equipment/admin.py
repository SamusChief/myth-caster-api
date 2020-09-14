""" Admin module for setting up models and forms in django-admin """
from django.contrib import admin

from .models import AdventuringGear, Armor, Tool, Weapon, WeaponProperty, WondrousItem

# Register your models here.
admin.site.register(AdventuringGear)
admin.site.register(Armor)
admin.site.register(Tool)
admin.site.register(Weapon)
admin.site.register(WeaponProperty)
admin.site.register(WondrousItem)
