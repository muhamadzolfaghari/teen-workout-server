from django.http import JsonResponse

from data.models import Accounts
from oauth2 import utils
from oauth2.utils import send_ok_response, send_unauth_response


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

            return send_ok_response(account_info)
        else:
            return send_unauth_response()
