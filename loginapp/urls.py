from django.http import JsonResponse, HttpResponse
from django.urls import path


def auth_with_google():
    return JsonResponse({})


urlpatterns = [
    path('', lambda response: HttpResponse("Hi to you!")),
    path('auth/google/', auth_with_google, name='hello_world')
]
