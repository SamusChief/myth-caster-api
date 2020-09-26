""" Filter module for handouts. Handouts also allow players to see the content. """
from django.db.models import Q

from .notes import NotesFilter


class HandoutsFilter(NotesFilter):
    """ Handouts filter. Allows all the same poeple to view as NotesFilter,
    and also party players. """
    @staticmethod
    def build_query(user):
        # owners and editors can see
        query = Q(owner=user.id) | Q(authorized_editors__in=[user.id])
        # Game masters can see
        query = query | Q(parties__game_masters__in=user.id)
        # Players can see
        query = query | Q(parties__players__in=user.id)
        return query
