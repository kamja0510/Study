import pickle

profile_file = open("profile.pickle", "wb") # wb = write binary
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile 에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb") # rb = read binary
profile = pickle.load(profile_file) # file 에 있는 정보를 profile에 저장
print(profile)
profile_file.close()

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding = "utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding = "utf8") as study_file:
    print(study_file.read())