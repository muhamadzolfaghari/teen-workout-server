from django.http import JsonResponse

from oatuh2 import utils


class OAuth2:
    def get_user_info(self, access_token: str):
        user_info = utils.get_user_info(access_token)

        if user_info:
            return JsonResponse(user_info)
        else:
            JsonResponse.status_code = 401
            return JsonResponse({})
