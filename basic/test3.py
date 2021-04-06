# 표준 체중을 구하는 프로그램
# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         *함수 명 : std_weight
#         *전달 값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시
from math import*

def std_weight(height, gender):
        if gender == "남자":
                en = round(pow(height*0.01,2)*22,2)
                print("키 {0}cm {1} 의 표준 체중은 {2} kg입니다.".format(height, gender, en))
        elif gender == "여자":
                en = pow(height*0.01,2)*21
                print("키 {0}cm {1} 의 표준 체중은 {2} kg입니다.".format(height, gender, en))
        else :
                print("입력오류 입니다.")

std_weight(175, "남자")
