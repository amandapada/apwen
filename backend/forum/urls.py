from django.urls import path
from .views import PostListCreateView, ForumPostDetailView, AddCommentView

urlpatterns = [
    path("posts/", PostListCreateView.as_view(), name="post-list-create"),
    path("posts/<int:pk>/", ForumPostDetailView.as_view(), name="post-detail"),
    path("posts/<int:post_id>/comment/", AddCommentView.as_view(), name="add-comment"),
]
