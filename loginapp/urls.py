from django.urls import path, include
# from django.views.generic import TemplateView
# from django.contrib.auth.views import LogoutView
from django.http import HttpResponse
# from .views import GoogleLogin

urlpatterns = [
    path('auth/google/', lambda request: HttpResponse('Hello World!'), name='hello_world')
]
