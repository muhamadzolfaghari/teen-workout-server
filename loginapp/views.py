import json

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from data.models import AgeRanges, Genders, AccountsProfiles, Accounts, Workouts, Foods
from oauth2.utils import verify_access_token, send_unauth_response, send_ok_response
from vercel_app import settings


def get_csrf(request):
    return render(request, 'loginapp/index.html')


def metadata(void):
    return JsonResponse({})
    # return JsonResponse({"age_ranges": age_ranges, 'genders': genders})


@csrf_exempt
def request_account_profile(request: WSGIRequest, *args, **kwargs):
    if request.method == 'GET':
        return get_account_profile(kwargs)
    elif request.method == 'POST':
        return post_account_profile(request)


def post_account_profile(request: WSGIRequest):
    body = json.loads(request.body)

    if not (
            body['gender'] or
            body['age_range'] or
            body['height'] and int(body['height']) or
            body['weight'] and int(body['weight']) or
            body['account_id'] and int(body['account_id']) or
            body['access_token'] and verify_access_token(body['access_token'])
    ):
        return send_unauth_response()

    account_profile = AccountsProfiles.objects.filter(account_id=body['account_id']).first()

    if account_profile:
        return send_ok_response()

    account = Accounts.objects.filter(id=body['account_id'])

    if account:
        gender = Genders.objects.filter(value=body['gender']).first()
        age_range = AgeRanges.objects.filter(value=body['age_range']).first()

        if gender and age_range and int(body['height']) and int(body['weight']):
            AccountsProfiles(
                account_id=body['account_id'],
                gender_id=gender.id,
                weight=body['weight'],
                height=body['height'],
                age_range_id=age_range.id
            ).save()
            account.update(is_completed=True)

            return send_ok_response()

    return send_unauth_response()


def get_account_profile(kwargs):
    account_id = kwargs.get('account_id')
    access_token = kwargs.get('access_token')

    if not (access_token or
            account_id and int(account_id) or
            verify_access_token(access_token)):
        return send_unauth_response()

    if account_id and int(account_id):
        account_profile = AccountsProfiles.objects.filter(account_id=account_id).first()

        if account_profile:
            gender = Genders.objects.filter(id=account_profile.gender_id).first()
            age_range = AgeRanges.objects.filter(id=account_profile.age_range_id).first()

            return send_ok_response({
                "height": account_profile.height,
                "weight": account_profile.weight,
                "gender": gender.value,
                "age_range": age_range.value,
            })

    return send_unauth_response()


def get_foods(request: WSGIRequest, *args, **kwargs):
    access_token = kwargs.get('access_token')

    if not verify_access_token(access_token):
        return send_unauth_response()

    foods = Foods.objects.select_related('meal_type')
    return send_ok_response({
        "results": [get_food_dict(food) for food in foods]
    })


def get_recommendations_foods(request: WSGIRequest, *args, **kwargs):
    access_token = kwargs.get('access_token')

    if not verify_access_token(access_token):
        return send_unauth_response()

    lunch = Foods.objects.filter(meal_type__value='lunch').first()
    dinner = Foods.objects.filter(meal_type__value='dinner').first()
    breakfast = Foods.objects.filter(meal_type__value='breakfast').first()

    return send_ok_response({"results": [
        get_food_dict(breakfast),
        get_food_dict(lunch),
        get_food_dict(dinner),
    ]})


def get_workouts(request: WSGIRequest, *args, **kwargs):
    access_token = kwargs.get('access_token')

    if not verify_access_token(access_token):
        return send_unauth_response()

    workouts = Workouts.objects.all()
    return send_ok_response({
        "results": [{
            "id": workout.id,
            "name": workout.name,
            "length": workout.length,
            "repeat": workout.repeat,
            "description": workout.description,
            "image": settings.MEDIA_URL + 'workouts/' + workout.image
        } for workout in workouts]
    })


def get_food_dict(food):
    return {
        "id": food.id,
        "name": food.name,
        "description": food.description,
        "meal_type": food.meal_type.value,
        "image": settings.MEDIA_URL + 'foods/' + food.image
    }
