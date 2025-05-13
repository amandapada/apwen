from django.urls import path
from .views import add_mentor_view, add_mentee_view, list_mentee_view, list_mentors_view

urlpatterns = [
    path('mentors/add/', add_mentor_view, name='add-mentor-view'),
    path('mentee/add/', add_mentee_view, name='add-mentee-view'),
    path('mentor/list/', list_mentors_view, name='list-mentor-view'),
    path('mentee/list/', list_mentee_view, name='list-mentee-view'),
]