from django.http import JsonResponse
from django.urls import path

urlpatterns = [
    path('auth/google/', lambda request: JsonResponse({'value': 'This is new update'}), name='hello_world')
]

