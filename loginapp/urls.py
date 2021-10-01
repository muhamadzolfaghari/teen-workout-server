from django.urls import path

from loginapp.views import Test
from oauth2.views import OAuth2

urlpatterns = [
    path('auth/google/<str:access_token>', OAuth2.get_account),
    path('', Test.as_view)
]
