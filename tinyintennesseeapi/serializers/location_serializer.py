from tinyintennesseeapi.models.location import Location
from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'title', 'electrical', 'address', 'county', 'water', 'septic', 'monthlyPrice', 'location_category')
        depth = 2