from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.maximize_window()


# 페이지 이동
url ="https://play.google.com/store/movies/top"
browser.get(url)

# 스크롤 내리기
# 해상도 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)")# 1920 x 1080

# 지정한 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 2초에 한번씩 스크롤 내림
interval = 2

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내리는 작업
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가저와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height
print("스크롤 완료")
# time.sleep(interval)
# browser.quit()


# ==============================================


import requests
from bs4 import BeautifulSoup

suop = BeautifulSoup(browser.page_source, "lxml")

movies = suop.find_all("div", attrs={"class":"Vpfmgd"}) # 리스트로 가저온다
print(len(movies))

# 영화정보 가져오기
for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    
    # 할인 전 가격 정보
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        print(title, "<할인 되지 않은 영화 제외>")
        continue
    # 할인된 가격
    price = movie.find("span", attrs={"class":})
    