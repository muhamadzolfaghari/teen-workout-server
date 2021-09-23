from rest_framework import serializers
from webapp.models import User
from loginapp.models import Login

class UserSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		#fields = ('title', 'slug', 'author', 'content', 'publish', 'status')
		#exclude = ('created', 'updated')
		fields = "__all__"


class LoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = Login
		fields = "__all__"