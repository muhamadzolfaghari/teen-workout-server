from django.urls import path
from oatuh2.views import OAuth2

urlpatterns = [
    path('auth/google/<str:access_token>', OAuth2.get_user_info)
]
