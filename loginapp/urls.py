from django.urls import path

from oauth2.views import OAuth2
from .views import metadata, get_csrf, request_account_profile

urlpatterns = [
    path('auth/google/<str:access_token>', OAuth2.get_account),
    path('metadata/', metadata),
    path('auth/csrf/', get_csrf),
    path('accounts/profile/<int:account_id>/<str:access_token>', request_account_profile),
    path('accounts/profile/', request_account_profile),
]
