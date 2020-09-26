""" Admin registration area for this app """
from django.contrib import admin

from .models import GameMasterFile, Handout, Notes


admin.site.register(GameMasterFile)
admin.site.register([Handout, Notes])
