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

        # Grab private users
        return queryset.filter(
            Q(is_private=False) | \
                (Q(owner=user.id) | Q(authorized_editors__in=[user.id]))
        )
