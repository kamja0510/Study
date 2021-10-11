# 주석은 #으로 한줄 씩 처리하거나(드래그 cirl+/) '''~''' 으로 여러줄 처리가능
animal = "강아지"
print("a"+"b")
print("a","b")
print(animal+" 니"+animal+"냐?") # 문자열 삽입 (숫자 문자열로 변환필요)
print(abs(-5)) # 절댓값
print(pow(4,2)) # 승수
print(max(5,12))
print(min(5,12))
print(round(3.14, 1)) # 1번째 자리까지 반올림
print(round(3.79))

from math import *
print(floor(4.88)) # 내림
print(ceil(4.88)) # 올림
print(sqrt(16)) # 제곱근

from random import*
print(random()) # 0.0 ~ 1.0 미만 임의의 값 생성
print(random()*10) # 0.0 ~ 10.0 미만 임의의 값 생성
print(int(random()*10)) # 0 ~ 10 미만 임의의 정수값 생성
print(int(random()*10+1)) # 1 ~ 10 이하 임의의 정수값 생성
print(randrange(1,45)) # 1 ~ 45 미만 임의의 정수값 생성
print(randint(1, 45)) # 1 ~ 45 이하 임의의 정수값 생성
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))

sentence = '''나는 소년이고, 파이썬은 쉬워요''' # "", '', """. ''' 문자열 표시
print(sentence)
print(sentence[3]) # 3번 인덱스 문자 슬라이스
print(sentence[0:3]) # 0번에서 2번 인덱스 문자 슬라이스 
print(sentence[:6]) # 처음부터 5번 인덱스 문자 슬라이스
print(sentence[10:]) # 10번 인덱스 문자부터 끝까지 슬라이스
print(sentence[-7:]) # 뒤에서 7번째 문자부터 끝까지 슬라이스

python = "Python is Amazing"
print(python.lower()) # 문자열 소문자로 변환
print(python.upper()) # 문자열 대문자로 변환
print(python[0].isupper()) # 대문자 맞는지 확인
print(len(python)) # 문자열 길이
print(python.replace("Python", "Java")) # 문자열 대체
index = python.index("on") # 'on' 문자열 시작의 인덱스 찾기
print(index)
index = python.index("n", index + 1) # 두번째 'n' 문자의 인덱스 찾기
print(index)
print(python.find("on")) # 'on' 문자열 시작의 인덱스 찾기
# .find 는 오류가 나면 -1을 출력하고, .index 는 오류가 나면 프로그램을 종료시킨다.
print(python.count("n")) # 'n' 갯수 출력

print("나는 %d살" % 20)
print("나는 %s을 좋아한다." % "파이썬")
print("Apple은 %c로 시작한다." % "A")
print("나는 %s색과 %s색을 좋아한다." % ("파랑", "빨강"))
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아한다.".format("파랑", "빨강"))
print("나는 {1}색과 {0}색을 좋아한다.".format("파랑", "빨강"))
print("나는 {age}살이며, {color}색을 좋아한다.".format(age = 20, color = "빨강"))
age = 20
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아한다.")
print("백문이 불여일견\n백견이 불여일타") # \n : 줄바꿈
print('저는 "나도코딩" 입니다.') # 따옴표 다른거 두개 쓰면 출력가능
print("Red Apple\rpine") # \r : 커서 맨 앞으로 이동
print("Redd\bApple") # \b : 백스페이스 누른 효과
print("Red\tApple") # \t : 탭 누른 효과