# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) #줄별로 일기, 한줄 읽고 커서는 다음줄로
# print(score_file.readline(), end="")
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# # while 문으로 전체 출력
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()    

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
