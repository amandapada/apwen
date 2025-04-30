from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatRoom(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mentor_chats")
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mentee_chats")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("mentor", "mentee")

    def __str__(self):
        return f"Chat between {self.mentor.username} and {self.mentee.username}"

class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} in {self.chat_room}"
