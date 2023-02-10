from bs4 import BeautifulSoup
import requests

url = "https://movie.naver.com/movie/bi/mi/review.naver?code=116234"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
# ul("rvw_list_area")>li>a>strong
ul = soup.find("ul", class_="rvw_list_area")
lis = ul.findAll("li")

for sequence, li in enumerate(lis, 1):
    print("[%dth] %s" % (sequence, li.a.string))
