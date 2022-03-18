from django.forms import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from tinyintennesseeapi.models import Builder
from tinyintennesseeapi.models.tituser import TitUser
from tinyintennesseeapi.serializers.builder_serializer import BuilderSerializer, CreateBuilderSerializer
from tinyintennesseeapi.serializers.user_serializer import UserSerializer

class UserView(ViewSet):
    def retrieve(self, request, pk):
        """Retrieve single user"""
        user = TitUser.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)