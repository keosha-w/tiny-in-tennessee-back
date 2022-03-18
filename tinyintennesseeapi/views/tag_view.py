from operator import truediv
from django.forms import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tinyintennesseeapi.models import Tag
from rest_framework import status
from tinyintennesseeapi.serializers import TagSerializer
from rest_framework.decorators import action


class TagView(ViewSet):
    
    def retrieve(self, request, pk):
        """Handle GET requests for single Builder"""
        tag = Tag.objects.get(pk=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)
    
    
    def list(self, request):
        """Get a list of tags"""
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)