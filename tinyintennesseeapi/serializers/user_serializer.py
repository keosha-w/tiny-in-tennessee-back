from tinyintennesseeapi.models.tituser import TitUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitUser
        fields = ('__all__')
        depth = 2
        