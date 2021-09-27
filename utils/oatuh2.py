import json
from typing import Any

import requests


def verify_access_token(access_token: str):
    if not access_token:
        return False

    url = f"https://www.googleapis.com/drive/v3/about?fields=user&access_token={access_token}"
    response = requests.get(url)

    if response.status_code == 200:
        return True
    else:
        return False


def user_info_decoder(s: Any):
    print(s)

def get_user_info(access_token: str):
    url = f"https://www.googleapis.com/drive/v3/about?fields=user&access_token={access_token}"
    response = requests.get(url)

    if response.status_code == 200:
        json.JSONDecoder.decode(response.json(), user_info_decoder)

