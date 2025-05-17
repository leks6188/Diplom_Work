from rest_framework import serializers
from posts.models import Comment, Post, Like

class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'text', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    post_comments = CommentPostSerializer(many=True, required = False, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user','text', 'image', 'created_at', 'post_comments', 'likes_count']
        read_only_fields = ['user', 'created_at' ]


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
        read_only_fields = ['user', 'created_at']

