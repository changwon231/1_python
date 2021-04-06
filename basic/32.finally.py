# 1. raise = 억지로 에러 만들기 
# 2. 에러 설정 하기 (직접 만들기)

class BigNumberError(Exception):
    def __init__(self, message):
        self.message = message


    def __str__(self):
        return self.message

try:
    print("한 질; 슷지 니늑; 잔영 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >=10:
        raise BigNumberError ("입력값 : {0}. {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한자리 숫자만 입력하세요")
    print(err)

# finally : 오류가 나도 안나도 무조건 실행되는 것
finally:
    print("계산기를 이용해 주셔서 감사합니다.")