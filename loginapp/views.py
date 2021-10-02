from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token, ensure_csrf_cookie
from django.views.decorators.http import require_POST

from data.models import AgeRanges, Genders, AccountsProfiles, Accounts
from oauth2.utils import verify_access_token


@requires_csrf_token
def get_csrf(request):
    return render(request, 'loginapp/index.html')


def metadata(void):
    return JsonResponse({})
    # return JsonResponse({"age_ranges": age_ranges, 'genders': genders})


# @csrf_exempt
# @ensure_csrf_cookie
@require_POST
def store_account_profile(wsgi: dict):
    print('is worked properly!')


    json = wsgi.json()
    if verify_access_token(json['access_token']):
        account = Accounts.objects.filter(id=json['user_id'])

        if account:
            gender = Genders.objects.filter(value=json['gender']).first()
            age_range = AgeRanges.objects.filter(value=json['age_range']).first()

            if gender and age_range and int(json['height']) and int(json['weight']):
                AccountsProfiles(
                    gender_id=gender.id,
                    weight=json['weight'],
                    height=json['height'],
                    age_range_id=age_range.id
                ).save()
                account.update(is_completed=True)

                return HttpResponse(status=200)

    else:
        JsonResponse.status_code = 401
        return JsonResponse({})
