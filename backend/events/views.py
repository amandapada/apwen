from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Event, Reminder
from .serializers import EventSerializer, ReminderSerializer

class EventListCreateView(generics.ListCreateAPIView):
    """List all events and create a new event (mentors only)"""
    queryset = Event.objects.all().order_by("date", "time")
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.is_mentor:
            return Response({"error": "Only mentors can create events."}, status=status.HTTP_403_FORBIDDEN)
        serializer.save(creator=self.request.user)

class EventDetailView(generics.RetrieveAPIView):
    """Retrieve a single event by ID"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReminderCreateView(generics.CreateAPIView):
    """Set a reminder for an event"""
    serializer_class = ReminderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        event_id = self.kwargs["pk"]
        event = get_object_or_404(Event, id=event_id)
        serializer.save(user=self.request.user, event=event)
