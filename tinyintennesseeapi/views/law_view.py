from operator import truediv
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.forms import ValidationError
from rest_framework import serializers, status
from tinyintennesseeapi.models import Law 
from tinyintennesseeapi.models.tituser import TitUser
from tinyintennesseeapi.serializers.law_serializer import CreateLawSerializer, LawSerializer

class LawView(ViewSet):
    def list(self, request):
        """Get a list of laws"""
        laws = Law.objects.all()
        serializer = LawSerializer(laws, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        user = TitUser.objects.get(user=request.auth.user)
        try:
            serializer = CreateLawSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message':ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)