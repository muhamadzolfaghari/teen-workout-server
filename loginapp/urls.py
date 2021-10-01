from django.urls import path

from .views import metadata, store_account_profile
from oauth2.views import OAuth2

urlpatterns = [
    path('auth/google/<str:access_token>', OAuth2.get_account),
    path('metadata', metadata),
    path('accounts/profile', store_account_profile)
]
