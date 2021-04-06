import requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[2].a.get_text()
# link = cartoons[0].a["href"] # 대괄호는 속성을 가져 올 수 있다.
# print(title)
# print("https://comic.naver.com"+link)


# 만화 제목과 링크 구하기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title + link)

# 평점 구하기
total_rate = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rate += float(rate)
print("전체점수 : ",total_rate)
print("평균점수 : ", total_rate / len(cartoons))    