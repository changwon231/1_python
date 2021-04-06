# glob : 경로 내의 폴더 / 파일 목록 조회
import glob
print(glob.glob("*.py"))


# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print("폴더를 삭제하였습니다.")
else:
    os.makedirs(folder) #폴더 생성
    print(folder, " 폴더를 생성했습니다.")

# 현재 디렉토리 내 존재하는 파일 표시 glab이랑 비슷
print(os.listdir())

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는", datetime.date.today())

today = datetime.date.today()
td = datetime.timedelta(days=100)# 100일 저장
print("우리가 만난지 100일은", today + td)
