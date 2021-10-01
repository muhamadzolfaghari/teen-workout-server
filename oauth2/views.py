from django.http import JsonResponse

from data.models import AgeRanges, Accounts
from oauth2 import utils


class OAuth2:
    def get_account(self, access_token: str):
        account_info = utils.get_accounts_info(access_token)
        # Accounts(account_info).save()



        if account_info:
            return JsonResponse(account_info)
        else:
            JsonResponse.status_code = 401
            return JsonResponse({})
