from django.urls import path
from .views import EventListCreateView, EventDetailView, ReminderCreateView

urlpatterns = [
    path("events/", EventListCreateView.as_view(), name="event-list"),
    path("events/<int:pk>/", EventDetailView.as_view(), name="event-detail"),
    path("events/<int:pk>/reminder/", ReminderCreateView.as_view(), name="set-reminder"),
]
