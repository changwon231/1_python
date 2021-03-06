import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title) # 타이틀 전부
# print(soup.title.get_text()) # 텍스트만

# print(soup.a) # 첫번째로 발견되는 a element 출력
# print(soup.a.attrs) # a element 의 속성 정보를 출력 태그 속성
# print(soup.a["href"]) # a element 의 href 속성 '값 정보를 출력

# print(soup.find("a", attrs={"class": "Nbtn_upload"}))# class : "" 안에 해당되는 "a" 엘리먼트 출력 
# print(soup.find(attrs={"class": "Nbtn_upload"})) # class="Nbtn_upload" 인 어떤 element 를 찾아줘

# print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a) # a 태그만 나온다.

### 형제 엘리먼트로 넘어가기

# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# print(rank1.next_sibling.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)

# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="열렙전사-2부 89화 - 버프")
print(webtoon)