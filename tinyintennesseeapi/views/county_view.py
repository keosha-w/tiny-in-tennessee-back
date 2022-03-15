from operator import truediv
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tinyintennesseeapi.models import County 
from tinyintennesseeapi.serializers.county_serializer import CountySerializer

class CountyView(ViewSet):
    def list(self, request):
        """Get a list of laws"""
        counties = County.objects.all()
        serializer = CountySerializer(counties, many=True)
        return Response(serializer.data)