from operator import truediv
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tinyintennesseeapi.models import Location, TitUser, County
from tinyintennesseeapi.serializers.location_serializer import LocationSerializer

class LocationView(ViewSet):
    def list(self, request):
        """Get a list of locations"""
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    