# 정규식 : 정해진 식 (regular expression) re

# 주민번호
# 90909-1101020

# 이메일 주소
# adfsdss@gmail.com

# 예) 교통사고 목격자 
import re
# 차량 번호는 4자리 글자
# ca?e
# care, cafe, case, cave ....

p = re.compile("ca.e" ) # <- 이 정규식 : "." 하나의 문자를 의미
                        #               (^ce) , "^" : 문자열의 시작 desk, destination(0) | fade(X)
                        #               (se$) , "$" : 문자열의 끝 > case, vase (0) | face (X)
    # print(m.group()) # 매칭되지 않으면 에러 발생
def print_match(m):
    if m:           # 에러가 나도 프로그램 실행
        print("m.group() : ", m.group()) # 일치하는 문자열 반환
        print("m.string :", m.string)  # 입력받은 문자열
        print("m.start() :", m.start()) # 일치하는 문자열의 시작 index
        print("m.end() : ", m.end()) # 일치하는 문자열의 끝 index
        print("m.span() : ", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")

# m = p.match("cagfeless") # match 이것과 매치 되는지 확인, 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

lst = p.findall("careless good cage") # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)

'''
    1. p = re.compile("원하는 형태")
    2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
    3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
    4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

    원하는 형태 : 저어규식
    . (ca.e) : 하나의 문자를 의미 > care, cafe, case (0) | caffe (X)
    ^ (^de)  : 문자열의 시작 > desk, destination (0) | fade(X)
    $ (se$)  : 문자열의 끝 > case, base (0) | face (X)

    w3school > run python > reguler expression
    python > re .. > 문서
'''