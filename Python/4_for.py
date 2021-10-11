for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))
for waiting_no in range(5):
    print("대기번호 : {0}".format(waiting_no))
for waiting_no in range(1, 6):
    print("대기번호 : {0}".format(waiting_no))
starbucks = ["토르", "아이언맨", "그루트"]
for customer in starbucks:
    print("나는 {0}이다".format(customer))

absent = [2, 5]
for student in range(1,11):
    if student in absent:
        continue
    print("{0}야, 책읽어봐라".format(student))

students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)
    