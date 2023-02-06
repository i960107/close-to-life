import requests

url = "https://search1.kakaocdn.net/argon/600x0_65_wr/ImZk3b2X1w8"

image_response = requests.get(url)

if image_response.status_code == 200:
    print("====이미지저장=====")
    # file pointer
    # b -> 텍스트가 아니라 binary파일로 읽기
    with open("test.jpg", "wb") as fp:
        # response에 content밖에 없나?
        fp.write(image_response.content)
