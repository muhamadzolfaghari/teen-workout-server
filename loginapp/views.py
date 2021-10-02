import json

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from data.models import AgeRanges, Genders, AccountsProfiles, Accounts
from oauth2.utils import verify_access_token


def get_csrf(request):
    return render(request, 'loginapp/index.html')


def metadata(void):
    return JsonResponse({})
    # return JsonResponse({"age_ranges": age_ranges, 'genders': genders})


# @ensure_csrf_cookie
@csrf_exempt
@require_POST
def store_account_profile(request: WSGIRequest):
    body = json.loads(request.body)

    if not int(body['account_id']):
        return send_unauth_response()

    if verify_access_token(body['access_token']):
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


def send_ok_response():
    return JsonResponse({})


def send_unauth_response():
    JsonResponse.status_code = 401
    return JsonResponse({})
