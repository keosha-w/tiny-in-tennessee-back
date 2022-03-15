from django.forms import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from tinyintennesseeapi.models import Builder
from tinyintennesseeapi.models.tituser import TitUser
from tinyintennesseeapi.serializers.builder_serializer import BuilderSerializer, CreateBuilderSerializer



class BuilderView(ViewSet):
    
    def retrieve(self, request, pk):
        """Handle GET requests for single Builder"""
        builder = Builder.objects.get(pk=pk)
        serializer = BuilderSerializer(builder)
        return Response(serializer.data)
    
    def list(self, request):
        """Get a list of builders"""
        builders = Builder.objects.all()
        # user = TitUser.objects.get(user=request.auth.user)
        serializer = BuilderSerializer(builders, many=True)
        return Response(serializer.data)


    def create(self, request):
        """Create a new builder"""

        user = TitUser.objects.get(user=request.auth.user)
        try:
            serializer = CreateBuilderSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message':ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)