from operator import truediv
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tinyintennesseeapi.models import Post
from tinyintennesseeapi.serializers.post_serializer import PostSerializer

class PostView(ViewSet):
    def list(self, request):
        """Get a list of posts"""
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    