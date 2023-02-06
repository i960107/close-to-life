from typing import Dict
import json
import requests


def send_message(access_token: str, template: Dict[str, str]) -> bool:
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {
        "Authorization": "Bearer " + access_token
    }
    template_object = {
        "template_object": json.dumps(template)
    }

    response = requests.post(url, headers=headers, params=template_object)

    if response.status_code != 200 or response.json()["result_code"] != 0:
        raise Exception(response.text)
    else:
        return True
