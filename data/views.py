from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import AgeRanges, Accounts, AccountsProfiles, Genders, Foods, MealTypes, Workouts, DailyWorkouts, WorkoutsDays #User, Gender,  Workout, Meal, Food
from .serializers import AgeRangesSerializer, AccountsSerializer, AccountsProfilesSerializer, GendersSerializer, FoodsSerializer, MealTypesSerializer, WorkoutsSerializer, DailyWorkoutsSerializer, WorkoutsDaysSerializer #UserSerializer, GenderSerializer,  WorkoutSerializer, MealSerializer, FoodSerializer
from oauth2.utils import send_unauth_response, send_ok_response
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


class WorkoutsDaysList(ListCreateAPIView):
	queryset = WorkoutsDays.objects.all()
	serializer_class = WorkoutsDaysSerializer


class WorkoutsDaysDetail(RetrieveUpdateDestroyAPIView):
	queryset = WorkoutsDays.objects.all()
	serializer_class = WorkoutsDaysSerializer

class AgeWorkouts(APIView):
	def get(self, request, age_range_id: int):
		if int(age_range_id):
			age_range = AgeRanges.objects.filter(id=age_range_id).first()
			if age_range:
				workouts = Workouts.objects.filter(age_range=age_range.id)
				if workouts:
					serializer = WorkoutsSerializer(workouts, many=True)
					return Response(serializer.data)
		return send_unauth_response()


class MealTypeFoods(APIView):
	def get(self, request, meal_type_id: int):
		if int(meal_type_id):
			meal_type = MealTypes.objects.filter(id=meal_type_id).first()
			if meal_type:
				foods = Foods.objects.filter(meal_type=meal_type.id)
				if foods:
					serializer = FoodsSerializer(foods, many=True)
					return Response(serializer.data)
		return send_unauth_response()


def get_bmi(request, profile_id: int):
	if int(profile_id):
		profile = AccountsProfiles.objects.filter(id=profile_id).first()
		if profile:
			bmi = profile.height ** 2 / profile.weight
			if bmi < 18.5:
				bmi_massage = 'Opps!! You weigh less than the standard amount. You need to have more nutrition and more proper. Do not worry, just eat the selected diet.'
			elif bmi < 24.9 and bmi > 18.4:
				bmi_massage = 'Yesss! Your fitness is great! It is better to maintain this fitness by following a diet and exercise.'
			elif bmi < 29.9 and bmi > 24.8:
				bmi_massage = 'mmmmmm! no it is not good! You are overweight and you need to return to a healthy and normal weight range with proper exercise and diet.'
			else:
				bmi_massage = 'No no... this is not good at all!! You are in the dangerous range of the standard body mass index and it indicates that you are obese. If you do not lose weight, you may face a variety of problems and diseases such as diabetes, cardiovascular disease, high cholesterol, etc. You should start exercising and eating right as soon as possible.'

			return JsonResponse({'bmi': bmi, 'massage': bmi_massage})

	return send_unauth_response()












# def update_profile(request: WSGIRequest):
# 	body = json.loads(request.body)
#
# 	if body['account_id'] and int(body['account_id']):
# 		account_profile = AccountsProfiles.objects.filter(id=body['account_id'])
#
# 		if body['weight'] and int(body['weight']):
# 			account_profile.update(weight=body['weight'])
#
# 		if body['height'] and int(body['height']):
# 			account_profile.update(height=body['height'])
#
# 		return send_ok_response()
#
# 	return send_unauth_response()
#
# def logout(request: WSGIRequest):
# 	body = json.loads(request.body)
# 	if body['account_id'] and int(body['account_id']):
# 		account = Accounts.objects.get(id=body['account_id'])
# 		if account:
# 			account.delete()
# 			return send_ok_response()
# 	return send_unauth_response()

# def erase_account(request: WSGIRequest)
# 	body = json.loads(request.body)
# 	if body['account_id'] and int(body['account_id']):
# 		account = Accounts.objects.get(id=body['account_id'])
# 		account_profile = AccountsProfiles.objects.get(id=body['account_id'])
# 		if account and account_profile:
# 			account

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
