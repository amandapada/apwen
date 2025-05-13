from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from mentors.views import list_mentee_view, list_mentors_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include('accounts.urls')),
    path("mentor/", include('mentors.urls')),
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    path('about-us', TemplateView.as_view(template_name="about.html"), name="about"),
    path('events', TemplateView.as_view(template_name="events.html"), name="events"),
    path('sign-in', TemplateView.as_view(template_name="sign_in.html"), name="sign_in"),
    path('sign-up', TemplateView.as_view(template_name="sign_up.html"), name="sign_up"),
    path('resources', TemplateView.as_view(template_name="resource.html"), name="sign_up"),
    path('mentorship', TemplateView.as_view(template_name="mentorship.html"), name="sign_up"),
    path('mentors', list_mentors_view, name='mentors'),
    path('add-mentor', TemplateView.as_view(template_name='add-mentor.html'), name='add-mentor'),
    path('mentees', list_mentee_view, name='mentees'),

    path('add-mentee', TemplateView.as_view(template_name='add-mentee.html'), name='add-mentee'),
    
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
