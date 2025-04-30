from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()

class MentorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="mentor_profile")
    department = models.CharField(max_length=255)
    level = models.CharField(max_length=50, blank=True, null=True)  # Graduate or specific level
    experience = models.TextField(blank=True, null=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.department}"

class MenteeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="mentee_profile")
    department = models.CharField(max_length=255)
    level = models.CharField(max_length=50)
    interests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.department}"

class MentorshipMatch(models.Model):
    mentee = models.ForeignKey(MenteeProfile, on_delete=models.CASCADE, related_name="matches")
    mentor = models.ForeignKey(MentorProfile, on_delete=models.CASCADE, related_name="mentees")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mentee.user.username} → {self.mentor.user.username}"
    
class Mentor(models.Model):
    name = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

