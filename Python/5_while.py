customer = "토르"
index = 5
while index >= 1: # while True : 무한 반복 cirl + c 누르면 강제종료
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")