""" Admin module for setting up models and forms in django-admin """
from django.contrib import admin

from .models import AdventuringGear, Armor, Tool, Weapon, WeaponProperty, WondrousItem

# Register your models here.
admin.register(AdventuringGear)
admin.register(Armor)
admin.register(Tool)
admin.register(Weapon)
admin.register(WeaponProperty)
admin.register(WondrousItem)
