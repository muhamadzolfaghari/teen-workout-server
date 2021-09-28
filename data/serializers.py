from rest_framework import serializers
from .models import User, Workout, AgeRange, Gender

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'


class AgeRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeRange
        fields = '__all__'


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'
