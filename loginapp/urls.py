from django.http import JsonResponse
from django.urls import path

urlpatterns = [
    path('auth/google/', lambda request: JsonResponse({'value': 12451545}), name='hello_world')
]
