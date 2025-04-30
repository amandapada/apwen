from django.urls import path
from .views import MentorListView, MenteeCreateView, MatchMentorView
# from .views import SomeMentorView

urlpatterns = [
    path("mentors/", MentorListView.as_view(), name="mentor-list"),
    path("mentees/register/", MenteeCreateView.as_view(), name="mentee-register"),
    path("match/", MatchMentorView.as_view(), name="mentor-match"),
    # path("example/", SomeMentorView.as_view(), name="example-view"),
]
