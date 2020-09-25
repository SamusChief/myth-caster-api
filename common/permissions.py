""" Permissions classes used by the app """
from rest_framework import permissions


SAFE_METHODS = ['GET', 'OPTIONS', 'HEAD']


class IsAdminOrReadOnly(permissions.IsAdminUser):
    """ Allow access to admin users, or read-only access if non-admin """
    def has_permission(self, request, view):
        parent_result = super(IsAdminOrReadOnly, self).has_permission(request, view)
        if request.method in SAFE_METHODS:
            return True
        return parent_result


class IsOwnerOrEditor(permissions.DjangoModelPermissionsOrAnonReadOnly):
    """
    Custom permissions handling class for Myth Caster.
    Checks the owner and authorized_editors fields of OwnedModel instances.
    If they exist, users can only put/post/delete if...
        - they are admins
        - they are either an owner or authorized editor
    """

    def has_object_permission(self, request, view, obj):
        """ Override object permissions to check editors and owners """
        super_result = super(IsOwnerOrEditor, self)\
            .has_object_permission(request, view, obj)
        method = request.method
        user = request.user

        # inactive users can't do anything
        if not user.is_active:
            return False

        # admin users bypass all permissions checks
        if user.is_superuser:
            return True

        # Check for an is_private flag. If its found and true, jump directly to checking
        # for owner/editor status. Ignore parent result in this case.
        if getattr(obj, 'is_private', False):
            return self._user_is_owner_or_authorized(user, obj, False)

        # Ignore GET, HEAD, OPTIONS for object checks
        if method in SAFE_METHODS:
            return super_result

        return self._user_is_owner_or_authorized(user, obj, super_result)

    @staticmethod
    def _user_is_owner_or_authorized(user, obj, default_return=False):
        """ Internal static method for determining if a user is an owner
        or editor of an object. Takes in a default_return for certain
        conditions."""
        # Get owner and editors, if they exist.
        # If they don't, this isn't an OwnedModel, and we should return our passed in default
        try:
            owner = getattr(obj, 'owner')
            authorized_editors = getattr(obj, 'authorized_editors')
        except AttributeError:
            return default_return

        # Check if current user is an authorized editor
        authorized_editors_ids = []
        if authorized_editors is not None:
            authorized_editors_ids = [a_e.id for a_e in authorized_editors.all()]

        # This means no owner has been set and editors is empty; effectively the
        # same condition as our AttributeError above
        if not owner and not authorized_editors_ids:
            return default_return

        return owner.id == user.id or user.id in authorized_editors_ids
