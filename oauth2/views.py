from django.http import JsonResponse

from data.models import Accounts
from oauth2 import utils


class OAuth2:
    def get_account(self, access_token: str):
        account_info = utils.get_accounts_info(access_token)

        if account_info:
            email = account_info['email']
            result = Accounts.objects.filter(email=email)

            if not result.count():
                Accounts(
                    email=account_info['email'],
                    name=account_info['name'],
                    image=account_info['image'],
                ).save()

            return JsonResponse(account_info)
        else:
            JsonResponse.status_code = 401
            return JsonResponse({})
