
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from posts.models import Comment, Post, Like
from posts.permission import IsOwner
from posts.serializers import PostSerializer, CommentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class PostViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]
    parser_classes = [MultiPartParser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self,serializer):
        serializer.save(user = self.request.user)


class CommentViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request, post_id):
        post = get_object_or_404(Post, id = post_id)
        user = request.user
        like, created = Like.objects.get_or_create(post=post,
                                                   author=user,
                                                   defaults = {'is_active': True})

        if created == False and like.is_active == True:
            return Response(
                {"status": "already liked"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            like.is_active = True
            like.save()
            return Response(
                {"status": "like"})

    def delete(self,request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user = request.user
        like = get_object_or_404(Like, post=post, author=user)

        if like.is_active:
            like.delete()
            return Response(
                {"status": "unlike"})

        else:
            like.delete()
            return Response({"status": "already unliked"},
                            status=status.HTTP_400_BAD_REQUEST)
