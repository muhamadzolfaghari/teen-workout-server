from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import AgeRanges, Accounts, AccountsProfiles, Genders#User, Gender,  Workout, Meal, Food
from .serializers import AgeRangesSerializer, AccountsSerializer, AccountsProfilesSerializer, GendersSerializer #UserSerializer, GenderSerializer,  WorkoutSerializer, MealSerializer, FoodSerializer
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