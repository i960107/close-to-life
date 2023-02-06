import requests
import yaml
import os


def save_image(sequence: int, image_url: str, file_name: str):
    image_response = requests.request("GET", document["image_url"])

    if not image_response.status_code == 200:
        print(str(sequence) + "번째 이미지 로드 실패")
    with open(download_path + "image" + str(sequence) + ".jpg", mode="wb") as fp:
        fp.write(image_response.content)


method = "POST"
host = "https://dapi.kakao.com"
url = "/v2/search/image"

with open("../conf.yaml", "r") as fp:
    config = yaml.load(fp, Loader=yaml.FullLoader)
rest_api_key = config["APP-KEY"]["KAKAO"]["REST-API-KEY"]
header = {"Authorization": "KakaoAK " + rest_api_key}

query_string = {"query": "고양이", "size": "50"}

# 이미지 검색 요청을 왜 POST로 보내지? POST와 다르게 GET은 암호화되지 않음
response = requests.request(method, host + url, headers=header, params=query_string)
response.raise_for_status()

download_path = os.getcwd() + "../res/downloads/"
if not os.path.exists(download_path):
    os.mkdir(download_path)

for sequence, document in enumerate(response.json()['documents'], 1):
    # json, yaml dictionary처럼 참조 가능
    save_image(sequence, download_path + "image" + str(sequence) + ".jpg", document["image_url"])
