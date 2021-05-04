# import pandas as pd/
import re
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome() #또는 chromedriver.exe
driver.implicitly_wait(5) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

# 페이지 가져오기(이동)
driver.get('http://its24.kr/sub01/01.php')

prd_name=[]
prd_price=[]

list_prod3 = ['#prod3 > option:nth-child(6)',
              '#prod3 > option:nth-child(7)',
              '#prod3 > option:nth-child(8)',
              '#prod3 > option:nth-child(9)',
              '#prod3 > option:nth-child(10)',
              '#prod3 > option:nth-child(11)',
              '#prod3 > option:nth-child(12)',
              '#prod3 > option:nth-child(13)',
              '#prod3 > option:nth-child(14)',
              '#prod3 > option:nth-child(15)',
              '#prod3 > option:nth-child(16)',
              '#prod3 > option:nth-child(17)',
              '#prod3 > option:nth-child(18)',
              '#prod3 > option:nth-child(19)',
              '#prod3 > option:nth-child(20)',
              '#prod3 > option:nth-child(21)',
              '#prod3 > option:nth-child(22)',
              '#prod3 > option:nth-child(23)']

list_prod4 = ['#prod4 > option:nth-child(2)',
              '#prod4 > option:nth-child(3)',
              '#prod4 > option:nth-child(4)',
              '#prod4 > option:nth-child(5)',
              '#prod4 > option:nth-child(6)',
              '#prod4 > option:nth-child(7)',
              '#prod4 > option:nth-child(8)',
              '#prod4 > option:nth-child(9)',
              '#prod4 > option:nth-child(10)',
              '#prod4 > option:nth-child(11)',
              '#prod4 > option:nth-child(12)',
              '#prod4 > option:nth-child(13)',
              '#prod4 > option:nth-child(14)',
              '#prod4 > option:nth-child(15)',
              '#prod4 > option:nth-child(16)',
              '#prod4 > option:nth-child(17)',
              '#prod4 > option:nth-child(18)']
# 요소 찾기 - 검색창찾고 키 전송
driver.find_element_by_css_selector('select#prod1').click()
driver.find_element_by_css_selector('#prod1 > option:nth-child(2)').click() ##7
driver.find_element_by_css_selector('select#prod2').click()
driver.find_element_by_css_selector('#prod2 > option:nth-child(2)').click() ##8
time.sleep(2)
driver.find_element_by_css_selector('select#prod3').click()
for b in list_prod3 :
    try:
        driver.find_element_by_css_selector(b).click()
        time.sleep(2)
        driver.find_element_by_css_selector('select#prod4').click()
        for a in list_prod4 :
            try:
                driver.find_element_by_css_selector(a).click()
                time.sleep(3)
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                prd_Name = soup.find_all(re.compile("h4"))
                prd_name2 = [each_line.get_text().strip() for each_line in prd_Name[:3]]
                prd_name.append(prd_name2[2])
                prd_Price = soup.findAll("dd", {"id": "ch_price"})
                prd_price2 = [each_line.get_text().strip() for each_line in prd_Price[:1]]
                prd_price.append(prd_price2[0])
            except:
                print("상품없음")
                break
    except:
        print("목록없음")
        break
# final = pd.DataFrame({'이름': prd_name, '매입가': prd_price})
print(final)
final.to_csv('it_pad.csv')
driver.quit()