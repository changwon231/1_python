''' 파일을 열고(open), 파일에 문자를 쓰고(w)고
    파일을 닫아준다. 항상 닫아야 함

'''

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()


# 이어서 쓰고 싶다. a 를 사용
score_file = open("score.txt", "a", encodi 
score_file.write("\n코딩 : 100")
score_file.close()

