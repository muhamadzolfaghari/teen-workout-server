from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from .views import GoogleLogin


urlpatterns = []