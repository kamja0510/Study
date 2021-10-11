weather =  input("오늘 날씨는 어때요?: ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요") 
else:
    print("준비물 필요 없음.")

temp = int(input("기온은 어때요?: "))
if 30 <= temp:
    print("too hot")
elif 10 <= temp and temp < 30:
    print("good")
elif 0 <= temp < 10:
    print("cold")
else:
    print("too cold")       