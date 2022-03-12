from operator import truediv
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tinyintennesseeapi.models import Law 
from tinyintennesseeapi.serializers.law_serializer import LawSerializer

class LawView(ViewSet):
    def list(self, request):
        """Get a list of laws"""
        laws = Law.objects.all()
        serializer = LawSerializer(laws, many=True)
        return Response(serializer.data)