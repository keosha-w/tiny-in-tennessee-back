from rest_framework import serializers
from tinyintennesseeapi.models import Law
from tinyintennesseeapi.models.locationCategory import LocationCategory

class LocationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationCategory
        fields = ('id', 'name')
        depth = 2