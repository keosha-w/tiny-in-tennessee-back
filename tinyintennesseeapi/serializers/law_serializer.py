from rest_framework import serializers
from tinyintennesseeapi.models import Law

class LawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = ('id', 'zoning', 'building', 'notes', 'user', 'county')
        depth = 2
        
class CreateLawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = ['id', 'zoning', 'building', 'notes', 'county']