from django.http import JsonResponse

from data.models import Accounts
from oauth2 import utils


class OAuth2:
    def get_account(self, access_token: str):
        account_info = utils.get_account_info(access_token)

        if account_info:
            email = account_info['email']
            account = Accounts.objects.filter(email=email).first()

            if not account:
                new_account = Accounts(
                    email=account_info['email'],
                    name=account_info['name'],
                    image=account_info['image'],
                )
                new_account.save()
                account_info['id'] = new_account.id
                account_info['is_completed'] = 'false'
            else:
                account_info['id'] = account.id
                account_info['is_completed'] = account.is_completed

            return JsonResponse(account_info)
        else:
            JsonResponse.status_code = 401
            return JsonResponse({})
