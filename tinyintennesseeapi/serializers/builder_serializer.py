from rest_framework import serializers
from tinyintennesseeapi.models import Builder

class BuilderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Builder
        fields = ('id', 'title', 'website', 'contact_info', 'user_id')
        depth = 1
