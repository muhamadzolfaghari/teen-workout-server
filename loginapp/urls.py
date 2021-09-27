from django.http import JsonResponse, HttpResponse
from django.urls import path
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

def auth_with_google():
    return JsonResponse({})

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

urlpatterns = [
    path('', lambda response: HttpResponse("Hi to you!")),
    #path('auth/google/', auth_with_google, name='hello_world')
    path('auth/google/', GoogleLogin.as_view(), name='google_login')

]
