from django.conf.urls.static import static
from django.urls import path

from oauth2.views import OAuth2
from vercel_app import settings
from .views import metadata, get_csrf, request_account_profile, get_workouts, get_foods, get_recommendations_foods

urlpatterns = [
      path('auth/google/<str:access_token>', OAuth2.get_account),
      path('metadata/', metadata),
      path('auth/csrf/', get_csrf),
      path('accounts/profile/<int:account_id>/<str:access_token>', request_account_profile),
      path('accounts/profile/', request_account_profile),
      path('workouts/<str:access_token>', get_workouts),
      path('foods/<str:access_token>', get_foods),
      path('recommendation-foods/<str:access_token>', get_recommendations_foods),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
