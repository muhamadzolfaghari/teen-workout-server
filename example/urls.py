from django.urls import path, include
from .views import home


app_name = 'hello'
urlpatterns = [
    path('', home, name = 'home'),
]