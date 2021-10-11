subway = ["유재석","조세호","박명수"] # 리스트
subway.remove("유재석")
print(subway)
print(subway.index("조세호"))
subway.append("하하")
print(subway)
subway.insert(1, "정형돈")
print(subway)
print(subway.pop()) # .pop 은 리스트에서 끝에 부터 빼고 출력하면 빠진 것이 출력된다.
print(subway)
print(subway.count("유재석"))


num_list = [5,2,4,3,1]
num_list.sort() # 정렬
print(num_list)
num_list.reverse() # 역순으로 배열
print(num_list)
num_list.clear() # 리스트 모두 지우기
print(num_list)
mix_list = [1, True, "감자"]

subway.extend(mix_list) # 리스트 확장
print(subway)

cabinet = {3:"유재석", 100:"김태호"}  # 사전
print(cabinet[3]) # 없는 키를 가져오려 하면 오류 출력 후 프로그램 종료시킴
print(cabinet.get(3)) # 없는 키를 가져오려 하면 None 이 출력되고 그 후 프로그램 계속 진행
print(cabinet.get(5, "사용가능"))
print(5 in cabinet)
cabinet[3] = "김종국"
cabinet[7] = "조세호"
print(cabinet)
del cabinet[100]
print(cabinet)
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())
cabinet.clear()
print(cabinet)

menu = ("돈까스", "치즈까스") # 튜플은 추가 안됌.
print(menu[0])
name, age, hobby = ("김종국", 20, "운동")
print(name, age, hobby)

my_set = {1,2,3,3,3} # 중복안됨, 순서없음. set = 집합.
print(my_set)
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])
print(java & python) # 교집합
print(java.intersection(python)) # 교집합
print(java | python) # 합집합
print(java.union(python)) # 합집합
print(java - python) # 차집합   
print(java.difference(python)) # 차집합
python.add("김태호") # 집합에 추가
print(python)
java.remove("양세형")
print(java)

drink = {"커피", "우유", "주스"}
print(drink, type(drink))
drink = list(drink)
print(drink, type(drink))
drink = tuple(drink)
print(drink, type(drink))
drink = set(drink)
print(drink, type(drink))
