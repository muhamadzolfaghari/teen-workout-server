from django.urls import path

from oauth2.views import OAuth2

urlpatterns = [
    path('auth/google/<str:access_token>', OAuth2.get_account),
    # path('/metadata', metadata)
]
