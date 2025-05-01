from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),  # Include authentication URLs
    path("api/mentors/", include("mentors.urls")),  # Include mentor-related URLs
    path("api/resources/", include("resources.urls")),  # Include resource-related URLs
    path("api/events/", include("events.urls")),  # Include events-related URLs
    path("api/chat/", include("chat.urls")),  # Include chat-related URLs
    path("api/forum/", include("forum.urls")),  # Include forum-related URLs
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    path('about-us', TemplateView.as_view(template_name="about.html"), name="about"),
    path('events', TemplateView.as_view(template_name="events.html"), name="events"),
    path('sign-in', TemplateView.as_view(template_name="sign_in.html"), name="sign_in"),
    path('sign-up', TemplateView.as_view(template_name="sign_up.html"), name="sign_up"),
    path('resources', TemplateView.as_view(template_name="resource.html"), name="sign_up"),
    path('mentorship', TemplateView.as_view(template_name="mentorship.html"), name="sign_up"),


    
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
