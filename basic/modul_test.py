# import modul
# modul.price(3)
# modul.price_morning(4)
# modul.price_solder(5)


# import modul as mo
# mo.price(3)
# mo.price_morning(4)
# mo.price_solder(5)

# from modul import price, price_morning
# price(5)
# price_morning(6)
# # price_solder(7) import 안되있어서 못씀

# from modul import price_solder as prs #<- 줄임표현
# prs(5)


# import traval.thailand
# trip_to = traval.thailand.ThailandPackage()
# trip_to.detail()

#from traval.vietnam import VietnamPackage
#trip_to = VietnamPackage()
#trip_to.detail()

#from traval import vietnam
#trip_to = VietnamPackage()
# trip_to.detail()

from traval import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# 패키지 or 파일 위치 확인
import inspect
import random
import math
print(inspect.getfile(random))
print(inspect.getfile(math))

