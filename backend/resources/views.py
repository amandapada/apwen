from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Resource
from .serializers import ResourceSerializer

# Create your views here.

class ResourceListCreateView(generics.ListCreateAPIView):
    """List all resources or create a new one"""
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

class ResourceDetailView(generics.RetrieveDestroyAPIView):
    """Retrieve or delete a specific resource"""
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

    def get_permissions(self):
        if self.request.method == "DELETE":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
