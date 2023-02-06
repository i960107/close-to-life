import requests
import yaml


def get_url_to_request_authorization_code(client_id: str, redirect_uri: str) -> str:
    # 브라우저에 url치고, redirect_uri에 포함된 code복사하기
    url = "https://kauth.kakao.com/oauth/authorize"

    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
    }

    response = requests.post(url, params=params)

    # post요청을 보냈는데 GET요청이 되는 이유?
    # redirect url이 있으면 get요청이 됨.
    # print(response.request.method)
    return (response.request.url)
    # print(response.request.headers)
    # print(response.request.body)
    # print(response.status_code)


def save_code(file_name: str) -> bool:
    print("redirect_url을 통해 응답받은 코드를 입력하세요 : ", end="")
    code = input()

    try:
        with open(file_name, "r") as fp:
            conf = yaml.load(fp, Loader=yaml.FullLoader)
        conf["KAKAO"]["AUTHORIZATION_CODE"] = code

        with open(file_name, "w") as fp:
            yaml.dump(conf, fp)

    except Exception:
        print("fail to save code")
        return False

    print("succeed to save code")
    return True


def load_code(file_name: str) -> str:
    with open(file_name, "r") as fp:
        conf = yaml.load(fp, Loader=yaml.FullLoader)
        code = conf["KAKAO"]["AUTHORIZATION_CODE"]
    return code
