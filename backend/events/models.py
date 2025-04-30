from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    
    def __str__(self):
        return self.title

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reminders")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="reminders")
    notification_time = models.DateTimeField()
    
    def __str__(self):
        return f"Reminder for {self.event.title} by {self.user.username}"
