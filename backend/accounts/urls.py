from django.urls import path
from .views import signup_view, login_view, logout_view

urlpatterns = [
    path('register/', signup_view, name='signup'),
    path('sign-in/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
