from operator import truediv
from django.forms import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tinyintennesseeapi.models import Post
from rest_framework import status
from tinyintennesseeapi.models.tag import Tag
from tinyintennesseeapi.models.tituser import TitUser
from tinyintennesseeapi.serializers.post_serializer import PostSerializer, CreatePostSerializer
from rest_framework.decorators import action


class PostView(ViewSet):
    
    def retrieve(self, request, pk):
        """Handle GET requests for single Builder"""
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    
    def list(self, request):
        """Get a list of posts"""
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a new builder"""

        user = TitUser.objects.get(user=request.auth.user)
        try:
            tags = []
            for tag in request.data['tags']:
                tags.append(Tag.objects.get(pk=tag))
            serializer = CreatePostSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user, tags=tags)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message':ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            post.title = request.data['title']
            post.content = request.data['content']
            post.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)    
        
    def destroy(self, request, pk):
        """Delete a post"""
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['post'], detail=True)
    def addtags(self, request, pk):
        """add post_tags to post"""
        post = Post.objects.get(pk=pk)
        tag = Tag.objects.get(pk=request.data['tag'])
        post.postTags.add(tag)
        return Response({'message': 'Gamer added'}, status=status.HTTP_201_CREATED)