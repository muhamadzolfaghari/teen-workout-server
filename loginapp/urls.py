import requests
from django.conf import settings
from django.http import HttpResponse
from django.urls import path

from loginapp.views import Authentication

urlpatterns = [
    path('auth/google/<str:access_token>', Authentication.oauth2)
]
