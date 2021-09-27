from django.http import JsonResponse
from django.urls import path


def auth_with_google():
    return JsonResponse({})


urlpatterns = [
    path('auth/google/', auth_with_google, name='hello_world')
]
