from rest_framework import serializers
from .models import Event, Reminder

class EventSerializer(serializers.ModelSerializer):
    creator_username = serializers.ReadOnlyField(source="creator.username")

    class Meta:
        model = Event
        fields = ["id", "title", "description", "date", "time", "creator", "creator_username"]

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ["id", "user", "event", "notification_time"]
