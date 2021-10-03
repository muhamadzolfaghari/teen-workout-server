import json

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from data.models import AgeRanges, Genders, AccountsProfiles, Accounts
from oauth2.utils import verify_access_token, send_unauth_response, send_ok_response


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
