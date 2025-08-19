from rest_framework import serializers
from .models import Post, Comment

# Post serializer
class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments_count']
        read_only_fields = ['id', 'created_at', 'updated_at']

        