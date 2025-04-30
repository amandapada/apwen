from django.urls import path
from .views import ResourceListCreateView, ResourceDetailView

urlpatterns = [
    path("", ResourceListCreateView.as_view(), name="resource-list"),
    path("<int:pk>/", ResourceDetailView.as_view(), name="resource-detail"),
]
