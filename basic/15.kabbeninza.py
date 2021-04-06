# end 는 이어서 출력하는 구문 
# 문장이 밑으로 안내려감

# def profile(name, age, lang1, lang2, lang3, lang4):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end = "")
#     print(lang1, lang2, lang3, lang4)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = "")
    for lang in language:
        print(lang, end=" ")
    print()
profile("유재석", 20, "python", "java", "c", "c++", "javascript")
profile("김태호", 25, "kotlin", "Swift", "", " ")