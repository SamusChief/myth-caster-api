""" Serializer module for the Handout model """
from common.serializers import OwnedModelSerializer
from game_mastering.models import Handout
from game_mastering.serializers import GameMasterFileSerializer


class HandoutSerializer(OwnedModelSerializer):
    """ Serializer for the Handout model. Includes secret content. """
    files = GameMasterFileSerializer(many=True, required=False)
    class Meta:
        model = Handout
        fields = '__all__'

    @staticmethod
    def should_hide_secrets(user, instance):
        """ Determine whether to hide the secret content and private files """
        # Superusers bypass the check and can see all information
        if getattr(user, 'is_superuser', False):
            return False

        # Anonymous users must have content hidden
        if not getattr(user, 'is_authenticated', False):
            return True

        # Users must be an owner, editor, or GM associated with this handout
        is_owner = instance.owner.id == user.id
        is_editor = user.id in [editor.id for editor in instance.authorized_editors.all()]
        is_game_master = user.id in [gm.id for gm in instance.get_parties_gms.all()]
        if is_owner or is_editor or is_game_master:
            return True

        return False

    def to_representation(self, instance):
        """ Override to account for secret data """
        result = super(HandoutSerializer, self).to_representation(instance)
        user = self.context.get('request.user', None)
        files = instance.files.all()

        # If we need to hide secret content, replace it with a string message.
        # Also, hide any private files
        if self.should_hide_secrets(user, instance):
            result['files'] = [GameMasterFileSerializer(f).data \
                for f in files if not f.is_private]
            result['secret_content'] = 'Hidden: you are not an owner, editor, or GM'

        return result
