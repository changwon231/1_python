# # 사전 : 단어, 단어 설명 MAP 이랑 똑같음 key 중복허용안됨
# cabinet = {3:"유재석", 100: "김태호"}
# print(cabinet[3])
# print(cabinet[100])
# print(cabinet.get(5))

# # [] 경우 값이 없을때 오류
# # get 인 경우 none 출력

# print(3 in cabinet)
# print(5 in cabinet)
cabinet = {"A-4":"유재석", 100: "김태호"}

print(cabinet["A-4"])
cabinet["A-4"] = "김종국"
cabinet["c-20"] = "조세호"
print(cabinet)

# 제거
del cabinet["A-4"]
print(cabinet)

#key 만 출력
print(cabinet.keys())

# value 만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 모두 제거
cabinet.clear()
print(cabinet)