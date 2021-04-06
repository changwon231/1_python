#modul 화  : 부품을 만드는 것 이라고 생각하면 됨 - 클래스

# 일반 가격
def price(people):
    print("{0} 명 가격은 {1}원 입니다.".format(people, people*10000))


# 조조 할인 가격
def price_morning(people):
    print("{0} 명 조조 할인 가격은 {1}원 입니다.".format(people, people*6000))

def price_solder(people):
        print("{0} 명 군인 가격은 {1}원 입니다.".format(people, people*5000))
