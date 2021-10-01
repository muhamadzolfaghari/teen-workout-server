from django.http import JsonResponse

from data.models import AgeRanges, Genders, AccountsProfiles
from oauth2.utils import verify_access_token
from django.http import JsonResponse, HttpResponse
import requests

def metadata(void):
    age_ranges = [{"id": row.id, "range": row.range} for row in AgeRanges.objects.all()]
    genders = [{"id": row.id, "range": row.title} for row in Genders.objects.all()]

    return JsonResponse({"age_ranges": age_ranges, 'genders': genders})

def datasaver(json : dict):
    if verify_access_token(json['access_token']) \
            and AgeRanges.objects.filter(id=json['age_range_id']) \
            and Genders.objects.filter(id=json['gender_id']) \
            and int(json['height']) \
            and int(json['weight']):

        AccountsProfiles(
            height=json['height'],
            weight=json['weight'],
            age_range=json['age_range_id'],
            gender_id=json['gender_id']
        ).save()

        return HttpResponse(status=200)

    else:
        JsonResponse.status_code = 401
        return JsonResponse({})
