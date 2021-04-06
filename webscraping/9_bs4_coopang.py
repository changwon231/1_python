import requests
import re
from bs4 import BeautifulSoup

url="https://browse.gmarket.co.kr/search?keyword=%eb%85%b8%ed%8a%b8%eb%b6%81&f=c:300021072"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
itmes = soup.find_all("div", attrs={"class":re.compile("^box__component box__component-itemcard box__component-itemcard--general")})
# print(itmes[0].find("span", attrs={"class":"text__item"}).get_text())
for item in itmes:
    # 사은품 상품 제외
    gift = item.find("span", attrs={"class":"box__tag box__tag-gift"})

    if gift:
        print("<<사은품 상품은 제외>>")
        continue
    name = item.find("span", attrs={"class":"text__item"}).get_text()
    price = item.find("strong", attrs={"class":"text text__value"}).get_text()    
    review = item.find("span", attrs={"class":"for-a11y"}) 
    if review: 
        review = review.get_text()
    else:
        review = "리뷰없음"
    num = item.find("span", attrs={"class":"text"}).get_text()  
    print(name, price, review, num)