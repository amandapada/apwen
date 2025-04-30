from rest_framework import serializers
from .models import ChatRoom, Message

class ChatRoomSerializer(serializers.ModelSerializer):
    mentor_username = serializers.ReadOnlyField(source="mentor.username")
    mentee_username = serializers.ReadOnlyField(source="mentee.username")

    class Meta:
        model = ChatRoom
        fields = ["id", "mentor", "mentee", "mentor_username", "mentee_username", "created_at"]

class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.ReadOnlyField(source="sender.username")

    class Meta:
        model = Message
        fields = ["id", "chat_room", "sender", "sender_username", "content", "timestamp"]
