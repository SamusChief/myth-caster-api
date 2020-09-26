""" Mixins for Game Master models """
from django.contrib.auth import get_user_model


class PartiesUsersMixin:
    """ Mixin for properties to grab party users for models that have a `parties` field """
    @property
    def parties_all_gms(self):
        """ Get the list of GMs who can see this handout """
        parties_gm_ids = self.parties.all().values_list('game_masters__id', flat=True)
        return get_user_model().objects.filter(id__in=parties_gm_ids)

    @property
    def parties_all_players(self):
        """ Get the list of players who can see this handout """
        parties_player_ids = self.parties.all().values_list('players__id', flat=True)
        return get_user_model().objects.filter(id__in=parties_player_ids)

    @property
    def parties_all_users(self):
        """ Get the list of all users who can see this handout """
        parties_player_ids = self.parties.all().values_list('players__id', flat=True)
        parties_gm_ids = self.parties.all().values_list('game_masters__id', flat=True)
        parties_all_users = (parties_player_ids | parties_gm_ids).distinct()
        return get_user_model().objects.filter(id__in=parties_all_users)
