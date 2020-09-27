""" Filters for Notes ViewSet """
from django.db.models import Q

from rest_framework import filters


class NotesFilter(filters.BaseFilterBackend):
    """ Filter that allows admins, owners, editors, and game masters to view notes """
    @staticmethod
    def build_query(user):
        """ Build our query using Q """
        # owners and editors can see
        query = Q(owner=user.id) | Q(authorized_editors__in=[user.id])
        # Game masters can see
        query = query | Q(parties__game_masters__in=[user.id])
        return query

    def filter_queryset(self, request, queryset, view):
        user = request.user

        # Admin users can see everything
        if user.is_superuser:
            return queryset

        return queryset.filter(self.build_query(user))
