from operator import truediv
from django.forms import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework import serializers, status
from tinyintennesseeapi.models import Location, TitUser, County, LocationCategory
from tinyintennesseeapi.serializers.location_serializer import LocationSerializer, CreateLocationSerializer

class LocationView(ViewSet):
    
    def retrieve(self, request, pk):
        """Handle GET requests for single Location"""
        location = Location.objects.get(pk=pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)
    
    def list(self, request):
        """Get a list of locations"""
        locations = Location.objects.all()
        approved = request.query_params.get('approved', None)
        if approved is not None:
            locations = locations.filter(is_approved=approved)
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def create(self, request):
        
        user = TitUser.objects.get(user=request.auth.user)
        try:
            serializer = CreateLocationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message':ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk):
        try:
            location = Location.objects.get(pk=pk)
            location.title = request.data['title']
            location.electrical = request.data['electrical']
            location.address = request.data['address']
            location.county_id = request.data['county_id']
            location.water = request.data['water']
            location.septic = request.data['septic']
            location.monthlyPrice = request.data['monthlyPrice']
            location.location_category_id = request.data['location_category']
            location.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except Location.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)       
        
    def destroy(self, request, pk):
        """Delete a location"""
        location = Location.objects.get(pk=pk)
        location.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['put'], detail=True)
    def approve_parking(self, request, pk):
        try:
            location = Location.objects.get(pk=pk)
            location.is_approved = request.data['is_approved']
            location.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except Location.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)