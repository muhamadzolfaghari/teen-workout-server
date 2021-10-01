import typing

from django.http import JsonResponse

from data.models import AgeRanges
from oauth2 import utils
from django.core import serializers


class OAuth2:
    def get_account(self, access_token: str):
        account_info = utils.get_accounts_info(access_token)
        # Accounts(account_info).save()

        age_ranges_rows = AgeRanges.objects.all()

        print(age_ranges_rows)


        return JsonResponse(age_ranges)

        # if account_info:
        #     return JsonResponse(account_info)
        # else:
        #     JsonResponse.status_code = 401
        #     return JsonResponse({})
