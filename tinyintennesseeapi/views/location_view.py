from operator import truediv
from django.forms import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from tinyintennesseeapi.models import Location, TitUser, County, LocationCategory
from tinyintennesseeapi.serializers.location_serializer import LocationSerializer, CreateLocationSerializer

class LocationView(ViewSet):
    
    def retrieve(self, request, pk):
        """Handle GET requests for single Builder"""
        location = Location.objects.get(pk=pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)
    
    def list(self, request):
        """Get a list of locations"""
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def create(self, request):
        # user = TitUser.objects.get(user=request.data['user'])
        # location_category = LocationCategory.objects.get(pk=request.data['location_category'])
        # county = County.objects.get(pk=request.data['county'])
        # location = Location.objects.create(
        #     title=request.data['title'],
        #     electrical=request.data['electrical'],
        #     address=request.data['address'],
        #     water=request.data['water'],
        #     septic=request.data['septic'],
        #     monthlyPrice=request.data['monthlyPrice'],
        #     user=user,
        #     location_category=location_category,
        #     county=county
        # )
        # serializer = LocationSerializer(location)
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        user = TitUser.objects.get(user=request.auth.user)
        try:
            serializer = CreateLocationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message':ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        