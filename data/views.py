from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import AgeRanges, Accounts, AccountsProfiles, Genders, Foods, MealTypes, Workouts, DailyWorkouts#User, Gender,  Workout, Meal, Food
from .serializers import AgeRangesSerializer, AccountsSerializer, AccountsProfilesSerializer, GendersSerializer, FoodsSerializer, MealTypesSerializer, WorkoutsSerializer, DailyWorkoutsSerializer #UserSerializer, GenderSerializer,  WorkoutSerializer, MealSerializer, FoodSerializer
# Create your views here.


class AgeRangesList(ListCreateAPIView):
	queryset = AgeRanges.objects.all()
	serializer_class = AgeRangesSerializer


class AgeRangesDetail(RetrieveUpdateDestroyAPIView):
	queryset = AgeRanges.objects.all()
	serializer_class = AgeRangesSerializer


class AccountsList(ListCreateAPIView):
	queryset = Accounts.objects.all()
	serializer_class = AccountsSerializer


class AccountsDetail(RetrieveUpdateDestroyAPIView):
	queryset = Accounts.objects.all()
	serializer_class = AccountsSerializer


class AccountsProfilesList(ListCreateAPIView):
	queryset = AccountsProfiles.objects.all()
	serializer_class = AccountsProfilesSerializer


class AccountsProfilesDetail(RetrieveUpdateDestroyAPIView):
	queryset = AccountsProfiles.objects.all()
	serializer_class = AccountsProfilesSerializer


class GendersList(ListCreateAPIView):
	queryset = Genders.objects.all()
	serializer_class = GendersSerializer


class GendersDetail(RetrieveUpdateDestroyAPIView):
	queryset = Genders.objects.all()
	serializer_class = GendersSerializer


class FoodsList(ListCreateAPIView):
	queryset = Foods.objects.all()
	serializer_class = FoodsSerializer


class FoodsDetail(RetrieveUpdateDestroyAPIView):
	queryset = Foods.objects.all()
	serializer_class = FoodsSerializer


class MealTypesList(ListCreateAPIView):
	queryset = MealTypes.objects.all()
	serializer_class = MealTypesSerializer


class MealTypesDetail(RetrieveUpdateDestroyAPIView):
	queryset = MealTypes.objects.all()
	serializer_class = MealTypesSerializer

class WorkoutsList(ListCreateAPIView):
	queryset = Workouts.objects.all()
	serializer_class = WorkoutsSerializer


class WorkoutsDetail(RetrieveUpdateDestroyAPIView):
	queryset = Workouts.objects.all()
	serializer_class = WorkoutsSerializer


class DailyWorkoutsList(ListCreateAPIView):
	queryset = DailyWorkouts.objects.all()
	serializer_class = DailyWorkoutsSerializer


class DailyWorkoutsDetail(RetrieveUpdateDestroyAPIView):
	queryset = DailyWorkouts.objects.all()
	serializer_class = DailyWorkoutsSerializer

# class UserList(ListCreateAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer
#
# class UserDetail(RetrieveUpdateDestroyAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer
#
# class GenderList(ListCreateAPIView):
# 	queryset = Gender.objects.all()
# 	serializer_class = GenderSerializer
#
# class GenderDetail(RetrieveUpdateDestroyAPIView):
# 	queryset = Gender.objects.all()
# 	serializer_class = GenderSerializer
#
# class WorkoutList(ListCreateAPIView):
# 	queryset = Workout.objects.all()
# 	serializer_class = WorkoutSerializer
#
# class WorkoutDetail(RetrieveUpdateDestroyAPIView):
# 	queryset = Workout.objects.all()
# 	serializer_class = WorkoutSerializer
#
# class FoodList(ListCreateAPIView):
# 	queryset = Food.objects.all()
# 	serializer_class = FoodSerializer
#
# class FoodDetail(RetrieveUpdateDestroyAPIView):
# 	queryset = Food.objects.all()
# 	serializer_class = FoodSerializer
#
# class MealList(ListCreateAPIView):
# 	queryset = Meal.objects.all()
# 	serializer_class = MealSerializer
#
# class MealDetail(RetrieveUpdateDestroyAPIView):
# 	queryset = Meal.objects.all()
# 	serializer_class = MealSerializer
