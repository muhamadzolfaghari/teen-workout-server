from rest_framework import serializers
from .models import AgeRanges #User, Workout, Gender, Food, Meal

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
#
#
# class WorkoutSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Workout
#         fields = '__all__'


class AgeRangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeRanges
        fields = '__all__'


# class GenderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Gender
#         fields = '__all__'
#
# class FoodSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Food
#         fields = '__all__'
#
# class MealSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Meal
#         fields = '__all__'