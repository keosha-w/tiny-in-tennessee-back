from django.forms import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from tinyintennesseeapi.models import Builder
from tinyintennesseeapi.models.tituser import TitUser
from tinyintennesseeapi.serializers.builder_serializer import BuilderSerializer, CreateBuilderSerializer
from rest_framework.decorators import action


class BuilderView(ViewSet):
    
    def retrieve(self, request, pk):
        """Handle GET requests for single Builder"""
        builder = Builder.objects.get(pk=pk)
        serializer = BuilderSerializer(builder)
        return Response(serializer.data)
    
    def list(self, request):
        """Get a list of builders"""
        builders = Builder.objects.all()
        approved = request.query_params.get('approved', None)
        if approved is not None:
            builders= builders.filter(is_approved=approved)
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
        
    def update(self, request, pk):
        try:
            builder = Builder.objects.get(pk=pk)
            builder.title = request.data['title']
            builder.website = request.data['website']
            builder.contact_info = request.data['contact_info']
            builder.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except Builder.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)            
        
    def destroy(self, request, pk):
        """Delete a builder"""
        builder = Builder.objects.get(pk=pk)
        builder.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['get'], detail=False)
    def adminList(self, request):
        """Get a list of builders"""
        builders = Builder.objects.all()
        serializer = BuilderSerializer(builders, many=True)
        return Response(serializer.data)
    
    @action(methods=['put'], detail=True)
    def approve_builder(self, request, pk):
        try:
            builder = Builder.objects.get(pk=pk)
            builder.is_approved = request.data['is_approved']
            builder.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except Builder.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)