import requests
from django.http import JsonResponse


def verify_access_token(access_token: str):
    if not access_token:
        return False

    url = f"https://www.googleapis.com/drive/v3/about?fields=user&access_token={access_token}"
    response = requests.get(url)

    if response.status_code == 200:
        return True
    else:
        return False


def get_account_info(access_token):
    url = f"https://www.googleapis.com/drive/v3/about?fields=user&access_token={access_token}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        user = data['user']
        name = user['displayName']
        email = user['emailAddress']
        image = user['photoLink']

        return {"name": name, "email": email, "image": image}


def send_ok_response(data=None):
    JsonResponse.status_code = 200
    return JsonResponse(data or {})


def send_unauth_response():
    JsonResponse.status_code = 401
    return JsonResponse({})
