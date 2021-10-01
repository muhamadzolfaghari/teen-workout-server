from django.urls import path
from .views import AgeRangesDetail, AgeRangesList, AccountsList, AccountsDetail #UserList, UserDetail, GenderList, GenderDetail, WorkoutDetail, WorkoutList, FoodList, FoodDetail, MealList, MealDetail


urlpatterns = [

    path('ages/', AgeRangesList.as_view()),
    path('ages/<int:pk>', AgeRangesDetail.as_view()),

    path('accounts/', AccountsList.as_view()),
    path('accounts/<int:pk>', AccountsDetail.as_view())

    # path('users/', UserList.as_view()),
    # path('users/<int:pk>', UserDetail.as_view()),
    #
    # path('gender/', GenderList.as_view()),
    # path('gender/<int:pk>', GenderDetail.as_view()),
    #
    # path('workout/', WorkoutList.as_view()),
    # path('workout/<int:pk>', WorkoutDetail.as_view()),
    #
    # path('food/', FoodList.as_view()),
    # path('food/<int:pk>', FoodDetail.as_view()),
    #
    # path('meal/', MealList.as_view()),
    # path('meal/<int:pk>', MealDetail.as_view())
]