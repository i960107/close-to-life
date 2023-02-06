from typing import Final, Dict

import manage_authorization_code
import manage_token
import send_me_text_message

import os

import yaml

TOKEN_FILENAME: Final = os.getcwd() + "/.." + "/res/kakao-token.json"
CONF_FILENAME: Final = os.getcwd() + "/../conf.yaml"

# conf 파일에서 필요한 정보 읽어오기
with open(CONF_FILENAME, "r") as fp:
    conf = yaml.load(fp, Loader=yaml.FullLoader)

redirect_uri = conf["KAKAO"]["REDIRECT_URI"]
client_id = conf["APP-KEY"]["KAKAO"]["REST-API-KEY"]

# authorization_code 받기
# url_for_authorization_code_request = manage_authorization_code.get_url_to_request_authorization_code(client_id,redirect_uri)
# print("다음 url에서 카카오 로그인을 통해 authorization_code를 받으세요 : " + url_for_authorization_code_request)
# manage_authorization_code.save_code(CONF_FILENAME)
authorization_code = manage_authorization_code.load_code(CONF_FILENAME)

# token 발급받고 저장하기
# tokens = manage_token.get_tokens(authorization_code, client_id, redirect_uri)
# manage_token.save_tokens(TOKEN_FILENAME, tokens)

# token 갱신하기
tokens = manage_token.load_tokens(TOKEN_FILENAME)
access_token = tokens["access_token"]
# updated_token = manage_token.update_tokens(TOKEN_FILENAME, client_id)


list_template = {
    "object_type": "list",
    "header_title": "방탈출 추천",
    "header_link": {"mobile_web_url": "www.naver.com"},
    "contents": [
        {
            "title": "서울이스케이프룸 홍대 2호점",
            "description": "아마존의 잃어버린 도시",
            "image_url": "https://mblogthumb-phinf.pstatic.net/MjAyMjA2MTNfMTIx/MDAxNjU1MDk3NTc5NDk2.0Nf1iaBv-UTN9nehh-hZRanzoF_JTFkITzDNe9DEx1Eg.jkkETjroIpWWfq3to2AoSC3OH0P2wPg8Pwo8s2OWgqwg.JPEG.wooruk_/AE92B352%25EF%25BC%258DF629%25EF%25BC%258D4B16%25EF%25BC%258D8363%25EF%25BC%258DE4AF48352A50%25EF%25BC%258D5503%25EF%25BC%258D000004E37C53CDCE.jpg?type=w800",
            "image_width": 640,
            "image_height": 640,
            "link": {
                "mobile_web_url": "https://www.seoul-escape.com",
            }
        },
        {
            "title": "키이스케이프 강남",
            "description": "살랑살랑 연구소",
            "image_url": "https://mblogthumb-phinf.pstatic.net/MjAyMjA2MTNfMTk3/MDAxNjU1MDk4MjQ0OTQ2.Dggpk6FSJKYEiPXsz7dN7keQjKqaCpdoTXMQIFKesEsg.IXEJbyegtSXscfyDqZpIsAOCAC0xoXLnUC1if4h-jKEg.JPEG.wooruk_/image%25EF%25BC%25BF4418364071521426639473.jpg?type=w800",
            "image_width": 640,
            "image_height": 640,
            "link": {
                "mobile_web_url": "https://keyescape.co.kr/web/home.php?go=main#self"
            }
        },
        {
            "title": "비밀의 화원 포레스트",
            "description": "미씽 스노우맨",
            "image_url": "https://mblogthumb-phinf.pstatic.net/MjAyMjA2MTNfMjY4/MDAxNjU1MDk4NjE1Mjc3.o_CqY9f23UqdGpwfOip_Ea6T9t80uuwggofZFpKoA8Ag.Fur1egiGTu44FgJJ3OXpCbLk4kpDusQbkoqH_K-ToGsg.JPEG.wooruk_/Pr%25EF%25BC%25BF1585751420.jpg?type=w800",
            "image_width": 640,
            "image_height": 640,
            "link": {
                "mobile_web_url": "http://m.secretgardenescape.com/index.html"
            }
        }
    ],
    "buttons": [
        {
            "title": "블로그 보기",
            "link": {
                "web_url": "https://m.blog.naver.com/wooruk_/222771256829"
            }
        }
    ]
}

text_template = {
    "object_type": "text",
    "text": "Hello,world!",
    "link": {"mobile_web_url": "https://www.naver.com"},
    "button_title": "자세히 보기"
}

send_me_text_message.send_message(access_token, text_template)
send_me_text_message.send_message(access_token, list_template)
