def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance,500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

def profile_1(name, age = 17, main_lang = "파이썬"): # 기본값 설정
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
        .format(name, age, main_lang))

profile_1("유재석")

def profile_2(name, age, main_lang):
    print(name, age, main_lang)

profile_2(main_lang = "파이썬", name = "유재석", age = 20) # 이렇게 선언하면 순서가 바뀌어도 상관없다.

def profile_3(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")
    for lang in language:
        print(lang, end = " ")
    print()

profile_3("유재석", 20, "Python", "Java", "C", "C++")
profile_3("김태호", 25, "Kotlin", "Swift")

gun = 10

def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))
