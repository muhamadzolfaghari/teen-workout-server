from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from .views import GoogleLogin


urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/google/', GoogleLogin.as_view(), name='google_login')
]