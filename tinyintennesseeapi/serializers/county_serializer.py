from rest_framework import serializers
from tinyintennesseeapi.models import County

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ('id', 'name')
        depth = 2