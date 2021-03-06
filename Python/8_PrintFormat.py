print("{0: >10}".format(-500)) # 빈 자리는 빈공간으로 두고, 오른쪽 정렬, 총10자리 확보
print("{0: >+10}".format(500)) # 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(-500))
print("{0:_<+10}".format(500)) # 응용 방법
print("{0:,}".format(1000000000)) # 세자리 마다 콤마 찍기
print("{0:+,}".format(-100000000)) # 부호까지 표시
print("{0:^<+30,}".format(1000000000)) # 배운것들 우선순위
print("{0:.2f}".format(5/3)) # 소수점 둘째 자리까지 반올림
