from typing import Dict
import json
import os
import datetime
import requests


def get_tokens(authorization_code: str, client_id: str, redirect_uri: str) -> Dict[str, str]:
    url = "https://kauth.kakao.com/oauth/token"
    params = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "code": authorization_code
    }

    response = requests.post(url, params=params)

    if response.status_code != 200:
        print("fail to issue token")
        raise Exception

    print("succeed to issue token")

    # response.json() type? Dict
    return response.json()


def save_tokens(file_name: str, tokens: Dict[str, str]):
    with open(file_name, "w") as fp:
        json.dump(tokens, fp)


def load_tokens(file_name: str) -> Dict[str, str]:
    with open(file_name, "r") as fp:
        tokens = json.load(fp)
    return tokens


def update_tokens(file_name: str, client_id: str) :
    tokens = load_tokens(file_name)

    url = "https://kauth.kakao.com/oauth/token"
    params = {
        "grant_type": "refresh_token",
        "client_id": client_id,
        "refresh_token": tokens["refresh_token"],
    }

    response = requests.post(url, params=params)

    if response.status_code != 200:
        print("error!" + response.json())
        tokens = None
    else:
        # 기존 파일 백업
        data = response.json()
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = file_name + "." + now
        os.rename(file_name, backup_filename)
        # 액세스 토큰 업데이트
        tokens["access_token"] = data["access_token"]
        tokens["expires_in"] = data["expires_in"]
        save_tokens(file_name, tokens)
    return tokens
