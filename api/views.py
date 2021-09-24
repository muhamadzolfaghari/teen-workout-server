from django.shortcuts import render
from webapp.models import User
from .serializers import UserSerializers
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.





class UserList(ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializers

class UserDetail(RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializers

class UserDetailCreate(CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializers

class UserDetailUpdate(UpdateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializers

class UserDetailDestroy(DestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializers