from django.urls import path

from oauth2.views import OAuth2
from .views import metadata, store_account_profile, get_csrf

urlpatterns = [
    path('auth/google/<str:access_token>', OAuth2.get_account),
    path('metadata/', metadata),
    path('accounts/profile/', store_account_profile),
    path('auth/csrf/', get_csrf)
]
