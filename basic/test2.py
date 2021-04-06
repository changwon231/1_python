# 당신은 Cocoa 서비스를 이용하는 택시 기사입니다. 
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간ㅏ은 5분 ~ 50분 사이의 난수로 정해집니다. 
# 조건2 : 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야됨

from random import *

customer = {}
num = 0
for i in range(50) :
    number = randrange(5,51)
    customer[i] = number
    count = " "
    if 5 <= number <= 15:
        count = "O"
        num +=1
    print("[{2}]{0} 번째 손님 (소요시간 {1}분)".format(i+1, customer.get(i), count))

print("총 납승 승객 : {0} 분".format(num))