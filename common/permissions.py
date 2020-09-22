""" Permissions classes used by the app """
from rest_framework import permissions


SAFE_METHODS = ['GET', 'OPTIONS', 'HEAD']

class OwnedPropertyPermission(permissions.DjangoModelPermissionsOrAnonReadOnly):
    """
    Custom permissions handling class for Myth Caster.
    Checks the owner and authorized_editors fields of OwnedModel instances.
    If they exist, users can only put/post/delete if...
        - they are admins
        - they are either an owner or authorized editor
    """

    def has_object_permission(self, request, view, obj):
        """ Override object permissions to check editors and owners """
        method = request.method
        user = request.user

        # Ignore GET, HEAD, OPTIONS
        if method in SAFE_METHODS:
            return True

        # Get owner and editors, if they exist.
        # If they don't, this isn't an OwnedModel, and we should return true
        try:
            owner = getattr(obj, 'owner')
            authorized_editors = getattr(obj, 'authorized_editors')
        except AttributeError:
            return True

        # Check if current user is an authorized editor
        authorized_editors_ids = []
        if authorized_editors is not None:
            authorized_editors_ids = [a_e.id for a_e in authorized_editors.all()]

        if not owner and not authorized_editors_ids:
            return True

        return owner.id == user.id or user.id in authorized_editors_ids
