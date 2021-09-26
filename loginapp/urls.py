from django.http import JsonResponse
from django.urls import path

urlpatterns = [
    path('auth/google/', lambda request: JsonResponse({'value': 'Hello World!'}), name='hello_world')
]
