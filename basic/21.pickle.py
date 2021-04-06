#피클 : 프로그램 상에서 사용하는 데이터를 파일 형태로 저장하는 것
import pickle

# b 는 바이너리, pickle 은 b 가 꼭 필요함
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)# profile에 있는 정보를 file 에 저장
# profile_file.close()

#파일 가져오기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) #파일에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()
