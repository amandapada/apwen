from rest_framework import serializers
from .models import ForumPost, Comment

class CommentSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Comment
        fields = ["id", "post", "user", "user_username", "content", "created_at"]

class ForumPostSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source="user.username")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = ForumPost
        fields = ["id", "user", "user_username", "title", "content", "created_at", "comments"]
