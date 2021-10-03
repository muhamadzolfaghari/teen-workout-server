from django.urls import path
from .views import AgeRangesDetail, AgeRangesList, AccountsList, AccountsDetail, AccountsProfilesList, AccountsProfilesDetail, GendersList, GendersDetail, FoodsList, FoodsDetail, MealTypesList, MealTypesDetail, WorkoutsList, WorkoutsDetail, DailyWorkoutsList, DailyWorkoutsDetail, AgeWorkouts, MealTypeFoods, get_bmi  #UserList, UserDetail, GenderList, GenderDetail, WorkoutDetail, WorkoutList, FoodList, FoodDetail, MealList, MealDetail


urlpatterns = [

    path('ages/', AgeRangesList.as_view()),
    path('ages/<int:pk>', AgeRangesDetail.as_view()),

    path('accounts/', AccountsList.as_view()),
    path('accounts/<int:pk>', AccountsDetail.as_view()),

    path('profiles/', AccountsProfilesList.as_view()),
    path('profiels/<int:pk>', AccountsProfilesDetail.as_view()),

    path('genders/', GendersList.as_view()),
    path('genders/<int:pk>', GendersDetail.as_view()),

    path('foods/', FoodsList.as_view()),
    path('foods/<int:pk>', FoodsDetail.as_view()),

    path('meal-types/', MealTypesList.as_view()),
    path('meal-types/<int:pk>', MealTypesDetail.as_view()),

    path('workouts/', WorkoutsList.as_view()),
    path('workouts/<int:pk>', WorkoutsDetail.as_view()),

    path('daily-workouts/', DailyWorkoutsList.as_view()),
    path('daily-workouts/<int:pk>', DailyWorkoutsDetail.as_view()),

    path('age-workouts/<int:age_range_id>/', AgeWorkouts.as_view()),
    path('meal-type-foods/<int:meal_type_id>/', MealTypeFoods.as_view()),

    path('bmi/<int:profile_id>/', get_bmi)

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