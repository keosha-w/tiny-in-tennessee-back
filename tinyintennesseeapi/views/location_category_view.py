from django.forms import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from tinyintennesseeapi.models import Location, TitUser, County, LocationCategory
from tinyintennesseeapi.serializers.location_category_serializer import LocationCategorySerializer


class LocationCategoryView(ViewSet):
    def list(self, request):
        """Get a list of LocationCategories"""
        locationCategories = LocationCategory.objects.all()
        serializer = LocationCategorySerializer(locationCategories, many=True)
        return Response(serializer.data)
        