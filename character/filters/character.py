""" Filters for Character ViewSet """
from django.db.models import Q

from rest_framework import filters


class CharacterOwnedOrAdminFilter(filters.BaseFilterBackend):
    """ Filter that allows admins, owners, or editors to view """
    def filter_queryset(self, request, queryset, view):
        user = request.user

        # Admin users bypass the filter
        if user.is_superuser:
            return queryset

        return queryset.filter(Q(owner=user) | Q(authorized_editors__contains=user))
