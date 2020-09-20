""" Weapon ViewSets """
import logging

from django.db import IntegrityError
from rest_framework import viewsets, decorators, response, exceptions, status

from equipment.models import Weapon, WeaponProperty
from equipment.serializers import WeaponSerializer, WeaponPropertySerializer

logger = logging.getLogger(__name__)


class WeaponViewSet(viewsets.ModelViewSet):
    """ ViewSet for Weapon. """
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'

    def get_serializer_class(self):
        """ Override so that DRF forms have proper inputs """
        if 'weapons/properties' in self.request.path:
            return WeaponPropertySerializer
        return WeaponSerializer

    def weapon_properties_list(self, request):
        """ List the WeaponProperty instances matching a query """
        filters = {}
        property_id = request.GET.get('id', None)
        name = request.GET.get('name', None)
        search = request.GET.get('search', None)

        # Build filters
        if property_id:
            filters['id'] = property_id
        if name:
            filters['name'] = name
        if search:
            filters['name__icontains'] = search
            filters['description__icontains'] = search

        # Build queryset and paginate it
        weapon_property_queryset = WeaponProperty.objects.filter(**filters)
        paginated_queryset = self.paginate_queryset(weapon_property_queryset)

        data = WeaponPropertySerializer(paginated_queryset, many=True).data
        return self.get_paginated_response(data)

    def weapon_properties_create(self, request):
        """ Use our serializer to create a validated WeaponProperty model """
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description')
        }
        serializer = self.get_serializer()
        try:
            instance = serializer.create(data)
        except IntegrityError as ex:
            raise exceptions.ValidationError(f'{str(ex)}')
        return response.Response(self.get_serializer(instance).data)

    def weapon_properties_update(self, request):
        """ Use our serializer to update a WeaponProperty model """
        # ID is required
        property_id = request.data.get('id', None)
        if not property_id:
            raise exceptions.ValidationError(
                '"id" is required to update a Weapon Property.',
                code=400
            )

        # Try to grab model, see if it exists
        try:
            instance = WeaponProperty.objects.get(id=property_id)
        except WeaponProperty.DoesNotExist as ex:
            raise exceptions.ValidationError(f'{str(ex)}')

        # Perform update
        data = {
            'id': instance.id,
            'name': request.data.get('name'),
            'description': request.data.get('description')
        }
        serializer = self.get_serializer()
        try:
            instance = serializer.update(instance, data)
        except IntegrityError as ex:
            raise exceptions.ValidationError(f'{str(ex)}')
        return response.Response(self.get_serializer(instance).data)

    def weapon_properties_delete(self, request):
        """ Make sure passed in id exists, and delete the model instance. """
        # ID is required
        property_id = request.GET.get('id', None)
        if not property_id:
            raise exceptions.ValidationError(
                '"id" is required to update a Weapon Property.',
                code=400
            )

        # Try to grab model, see if it exists
        try:
            instance = WeaponProperty.objects.get(id=property_id)
        except WeaponProperty.DoesNotExist as ex:
            raise exceptions.ValidationError(f'{str(ex)}')

        instance.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    @decorators.action(detail=False, methods=['get', 'put', 'post', 'delete'])
    def properties(self, request):
        """
        A simple 'subviewset' implementation for WeaponProperty models
        TODO implement permissions check
        """
        logger.info(self.get_serializer().data)
        if request.method == 'GET':
            return self.weapon_properties_list(request)
        if request.method == 'POST':
            return self.weapon_properties_create(request)
        if request.method == 'PUT':
            return self.weapon_properties_update(request)
        if request.method == 'DELETE':
            return self.weapon_properties_delete(request)
