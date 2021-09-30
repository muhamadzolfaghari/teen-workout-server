from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User, Gender, AgeRange, Workout, Meal, Food
from .serializers import UserSerializer, GenderSerializer, AgeRangeSerializer, WorkoutSerializer, MealSerializer, FoodSerializer
# Create your views here.
class UserList(ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class GenderList(ListCreateAPIView):
	queryset = Gender.objects.all()
	serializer_class = GenderSerializer

class GenderDetail(RetrieveUpdateDestroyAPIView):
	queryset = Gender.objects.all()
	serializer_class = GenderSerializer

class AgeRangeList(ListCreateAPIView):
	queryset = AgeRange.objects.all()
	serializer_class = AgeRangeSerializer

class AgeRangeDetail(RetrieveUpdateDestroyAPIView):
	queryset = AgeRange.objects.all()
	serializer_class = AgeRangeSerializer

class WorkoutList(ListCreateAPIView):
	queryset = Workout.objects.all()
	serializer_class = WorkoutSerializer

class WorkoutDetail(RetrieveUpdateDestroyAPIView):
	queryset = Workout.objects.all()
	serializer_class = WorkoutSerializer

class FoodList(ListCreateAPIView):
	queryset = Food.objects.all()
	serializer_class = FoodSerializer

class FoodDetail(RetrieveUpdateDestroyAPIView):
	queryset = Food.objects.all()
	serializer_class = FoodSerializer

class MealList(ListCreateAPIView):
	queryset = Meal.objects.all()
	serializer_class = MealSerializer

class MealDetail(RetrieveUpdateDestroyAPIView):
	queryset = Meal.objects.all()
	serializer_class = MealSerializer