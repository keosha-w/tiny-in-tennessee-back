from tinyintennesseeapi.models.location import Location
from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'title', 'electrical', 'address', 'county_id', 'water', 'septic', 'monthlyPrice', 'location_category_id')
        depth = 1