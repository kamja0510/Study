score_file = open("score.txt", "w", encoding = "utf8") # 파일 쓰기
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)
score_file.close()

score_file = open("score.txt", "a", encoding = "utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8") # 줄별로 읽고 커서 아래줄로 이동
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8") # 몇 줄 일지 모를때 파일 읽기
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end = "")
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
