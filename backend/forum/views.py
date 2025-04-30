from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import ForumPost, Comment
from .serializers import ForumPostSerializer, CommentSerializer

class PostListCreateView(generics.ListCreateAPIView):
    """Handles listing and creating forum posts"""
    serializer_class = ForumPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = ForumPost.objects.all().order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ForumPostDetailView(generics.RetrieveAPIView):
    """Retrieve a single forum post along with its comments"""
    serializer_class = ForumPostSerializer
    permission_classes = [permissions.AllowAny]
    queryset = ForumPost.objects.all()

class AddCommentView(generics.CreateAPIView):
    """Add a comment to a forum post"""
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        post_id = kwargs["post_id"]
        post = get_object_or_404(ForumPost, id=post_id)

        comment = Comment.objects.create(
            post=post,
            user=request.user,
            content=request.data.get("content", ""),
        )

        return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)
