""" Admin panel regitsrtion for character app """
from django.contrib import admin

from .models import Ancestry, Background, Character

# Register your models here.
admin.site.register(Ancestry)
admin.site.register(Background)
admin.site.register(Character)
# TODO
