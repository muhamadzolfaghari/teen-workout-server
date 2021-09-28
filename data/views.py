from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User, Gender, AgeRange, Workout
from .serializers import UserSerializer, GenderSerializer, AgeRangeSerializer, WorkoutSerializer
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