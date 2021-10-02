from django.urls import path

from oauth2.views import OAuth2
from .views import metadata, register_account_profile, get_csrf, account_info

urlpatterns = [
    path('auth/google/<str:access_token>', OAuth2.get_account),
    path('metadata/', metadata),
    path('accounts/profile/', register_account_profile),
    path('auth/csrf/', get_csrf),
    path('accounts/profile/<int:id>/<str:access_token>', account_info)
]
