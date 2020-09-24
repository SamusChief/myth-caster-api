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

    def has_object_permission(self, request, view, obj, **kwargs):
        """ Override object permissions to check editors and owners """
        super_result = super(OwnedPropertyPermission, self).has_object_permission(**kwargs)
        method = request.method
        user = request.user

        # inactive users can't do anything
        if not user.is_active:
            return False

        # admin users bypass all permissions checks
        if user.is_superuser:
            return True

        # Ignore GET, HEAD, OPTIONS for object checks
        if method in SAFE_METHODS:
            return super_result

        # Get owner and editors, if they exist.
        # If they don't, this isn't an OwnedModel, and we should return the parent result
        try:
            owner = getattr(obj, 'owner')
            authorized_editors = getattr(obj, 'authorized_editors')
        except AttributeError:
            return super_result

        # Check if current user is an authorized editor
        authorized_editors_ids = []
        if authorized_editors is not None:
            authorized_editors_ids = [a_e.id for a_e in authorized_editors.all()]

        if not owner and not authorized_editors_ids:
            return super_result

        return owner.id == user.id or user.id in authorized_editors_ids
