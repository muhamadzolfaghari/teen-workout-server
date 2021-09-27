import requests
from django.http import JsonResponse


class Authentication:
    def oauth2(self, access_token: str):
        url = f"https://www.googleapis.com/drive/v3/about?fields=user&access_token={access_token}"
        response = requests.get(url)

        if response.status_code == 200:
            JsonResponse.status_code = 200
            return JsonResponse(response.json())
        else:
            JsonResponse.status_code = 401
            return JsonResponse({})
