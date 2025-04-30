from rest_framework import serializers
from .models import MentorProfile, MenteeProfile, MentorshipMatch

class MentorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorProfile
        fields = "__all__"

class MenteeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenteeProfile
        fields = "__all__"

class MentorshipMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorshipMatch
        fields = "__all__"
        
from .models import Mentor

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'
