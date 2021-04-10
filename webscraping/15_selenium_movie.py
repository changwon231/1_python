import requests
from bs4 import BeautifulSoup

url ="https://play.google.com/store/movies/top"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    }


res = requests.get(url, headers=headers)
res.raise_for_status()
suop = BeautifulSoup(res.text, "lxml")

movies = suop.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

# # 정보가 제대로 안불러와서 파일로 찾아보자
# with open("movie.html", "w", encoding="utf8") as f:
#     # f.write(res.text)
#     f.write(suop.prettify())# 보기 편하게 정리해주는 함수

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)

