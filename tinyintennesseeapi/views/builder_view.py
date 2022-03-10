from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tinyintennesseeapi.models import Builder, TitUser
from tinyintennesseeapi.serializers.builder_serializer import BuilderSerializer

class BuilderView(ViewSet):
    def list(self, request):
        """Get a list of builders"""
        builders = Builder.objects.all()
        # user = TitUser.objects.get(user=request.auth.user)
        serializer = BuilderSerializer(builders)
        return Response(serializer.data)
