from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatRoomListView(generics.ListAPIView):
    """List all chat rooms for the logged-in user"""
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ChatRoom.objects.filter(mentor=self.request.user) | ChatRoom.objects.filter(mentee=self.request.user)

class CreateChatRoomView(generics.CreateAPIView):
    """Create a new chat room (Mentees can initiate a chat with a Mentor)"""
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        mentee = request.user
        mentor_id = request.data.get("mentor")
        
        if not mentor_id:
            return Response({"error": "Mentor ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        mentor = get_object_or_404(User, id=mentor_id, is_mentor=True)

        chat_room, created = ChatRoom.objects.get_or_create(mentor=mentor, mentee=mentee)

        if created:
            return Response(ChatRoomSerializer(chat_room).data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Chat room already exists"}, status=status.HTTP_400_BAD_REQUEST)

class MessageListView(generics.ListAPIView):
    """Retrieve messages in a chat room"""
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        chat_room_id = self.kwargs["room_id"]
        return Message.objects.filter(chat_room_id=chat_room_id).order_by("timestamp")

class SendMessageView(generics.CreateAPIView):
    """Send a message in a chat room"""
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        chat_room_id = kwargs["room_id"]
        chat_room = get_object_or_404(ChatRoom, id=chat_room_id)

        if request.user not in [chat_room.mentor, chat_room.mentee]:
            return Response({"error": "You are not part of this chat room"}, status=status.HTTP_403_FORBIDDEN)

        message = Message.objects.create(
            chat_room=chat_room,
            sender=request.user,
            content=request.data.get("content", ""),
        )

        return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)
