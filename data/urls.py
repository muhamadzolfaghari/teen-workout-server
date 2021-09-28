from django.urls import path
from .views import UserList, UserDetail, GenderList, GenderDetail, AgeRangeDetail, AgeRangeList, WorkoutDetail, WorkoutList


urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),

    path('gender/', GenderList.as_view()),
    path('gender/<int:pk>', GenderDetail.as_view()),

    path('age/', AgeRangeList.as_view()),
    path('age/<int:pk>', AgeRangeDetail.as_view()),

    path('workout/', WorkoutList.as_view()),
    path('workout/<int:pk>', WorkoutDetail.as_view())
]