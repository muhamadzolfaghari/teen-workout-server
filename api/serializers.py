from rest_framework import serializers
from webapp.models import User

class UserSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		#fields = ('title', 'slug', 'author', 'content', 'publish', 'status')
		#exclude = ('created', 'updated')
		fields = "__all__"

