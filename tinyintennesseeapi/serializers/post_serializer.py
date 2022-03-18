from tinyintennesseeapi.models.post import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'date_posted', 'is_approved', 'user', 'tags')
        depth = 2
        
        
   
class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'date_posted', 'is_approved']