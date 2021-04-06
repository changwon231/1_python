class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):      
        print("Flyable 생성자")


# 두개 이상의 부모클래스가 있을 경우 super 를 쓸 경우 뒷클래스는 호출 안됨
class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)


# 드랍쉽
dropship = FlyableUnit()          