from django.forms import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status

class AdminView(ViewSet):
    """Admin view"""
    