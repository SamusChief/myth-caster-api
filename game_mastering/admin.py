""" Admin registration area for this app """
from django.contrib import admin

from .models import File, Handout, Notes


admin.site.register(File)
admin.site.register([Handout, Notes])
