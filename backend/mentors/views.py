from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import MentorProfile, MenteeProfile, MentorshipMatch
from .serializers import MentorProfileSerializer, MenteeProfileSerializer, MentorshipMatchSerializer
from rest_framework.permissions import AllowAny
from .models import Mentor
from .serializers import MentorSerializer

# class MentorListView(generics.ListAPIView):
#     """Get a list of available mentors"""
#     queryset = MentorProfile.objects.filter(availability=True)
#     serializer_class = MentorProfileSerializer
    # permission_classes = [IsAuthenticated]
class MentorListView(generics.ListAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [AllowAny]

class MenteeCreateView(generics.CreateAPIView):
    """Register a mentee profile"""
    queryset = MenteeProfile.objects.all()
    serializer_class = MenteeProfileSerializer
    permission_classes = [IsAuthenticated]

class MatchMentorView(generics.CreateAPIView):
    """Match a mentee with an available mentor"""
    serializer_class = MentorshipMatchSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Ensure the mentee exists for the requesting user
        mentee = get_object_or_404(MenteeProfile, user=request.user)

        # Find an available mentor in the same department
        available_mentors = MentorProfile.objects.filter(department=mentee.department, availability=True)

        if available_mentors.exists():
            mentor = available_mentors.first()  # Select the first available mentor
            match, created = MentorshipMatch.objects.get_or_create(mentee=mentee, mentor=mentor)

            return Response(
                {
                    "message": "Mentor matched successfully!",
                    "match_id": match.id,
                    "mentor": MentorProfileSerializer(mentor).data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"message": "No available mentors in your department"},
            status=status.HTTP_404_NOT_FOUND,
        )
