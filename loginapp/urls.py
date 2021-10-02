from django.urls import path

from oauth2.views import OAuth2
from .views import metadata, register_account_profile, get_csrf, get_account_profile

urlpatterns = [
    path('auth/google/<str:access_token>', OAuth2.get_account),
    path('metadata/', metadata),
    path('accounts/profile/', register_account_profile),
    path('auth/csrf/', get_csrf),
    path('accounts/profile/<int:account_id>/<str:access_token>', get_account_profile)
]
