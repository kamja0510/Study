print("Python", "Java", sep = ",", end = "?")
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file = sys.stdout) # 잘 모르겟음 아직
print("Python", "Java", file = sys.stderr)

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep = ":") # 정렬

for num in range(1, 11):
    print("대기번호 : " +str(num).zfill(3)) # 공간 확보후 빈공간 0으로 채우기

answer = input("아무 값이나 입력하세요 : ") # 입력
print("입력하신 값은 " + answer + "입니다.")

 