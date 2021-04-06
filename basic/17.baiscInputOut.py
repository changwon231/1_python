import sys

# print("Python", "Java", "JavaScript", sep=" , ",end=" ")
# print("무엇이 더 재밌을까요?")

# print("Python", "Java", file=sys.stdout)
# print("Python","Java", file=sys.stderr) #에러 처리 가능

# scores = {"수학":0, "영어": 20, "코딩": 100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4) ,sep=":") # ljust = 왼쪽정열 8간다, rjust 오른쪽 정열

# 은행 대기 순번표
# 001, 002, 003, ....
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3)) # 3만큼 크기를 지정하는데 빈공간은 0으로 채움

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")
