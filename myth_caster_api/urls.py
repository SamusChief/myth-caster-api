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

from rest_framework import routers

from administration.views import UserViewset
from character.views import AncestryViewset, SubAncestryViewset, BackgroundViewset, \
    CharacterClassViewset, ArchetypeViewset, CharacterViewset, FeatureViewset

urlpatterns = [
    path('api/django-admin/', admin.site.urls),
]

router = routers.DefaultRouter()
# Admin Routes
router.register(r'api/administration/user', UserViewset, basename='user-readonly-viewset')

# Character Routes
router.register(r'api/ancestry', AncestryViewset)
router.register(r'api/ancestry/subancestry', SubAncestryViewset)
router.register(r'api/background', BackgroundViewset)
router.register(r'api/class', CharacterClassViewset)
router.register(r'api/class/archetype', ArchetypeViewset)
router.register(r'api/character', CharacterViewset)
router.register(r'api/feature', FeatureViewset)

urlpatterns += router.urls
