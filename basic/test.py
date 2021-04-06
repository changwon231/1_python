# site = "http://google.com"
# site = site.replace("http://", "")
# print(site)
# number = site.find(".")
# print(number)
# site = site[ : number]
# print(site)
# num1 = site[:3]
# num2 = len(site)
# num3 = site.count("e")

# print(f"{num1}{num2}{num3}!")

# ㅏㄷㅇ신의 학굥서는 파이썬 코딩 대회를 주최합니다. 
# 참석률을 높이기 위해 딧글 이벤트를 진행하기로 하였습니다. 
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다. 

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용
from random import *
#id 리스트
id = list(range(1,21))
print(type(id))

# 치킨 당첨자 한번 섞은 후 1개 추출
shuffle(id)
chickn = sample(id, 1)

# 뽑힌 사람 제거 후 3개 추출
id.remove(chickn[0])
coffie = sample(id, 3)

#출력
print("-- 당첨자 발표 --")
print( "치킨 당첨자 : " + str(chickn))
print("커피 당첨자 :" + str(coffie))
print("-- 축하합니다. --")
