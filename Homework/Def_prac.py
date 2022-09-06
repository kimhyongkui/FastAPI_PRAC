from fastapi import FastAPI
import itertools

app = FastAPI()

# 함수를 만든다
# 함수속에 리스트를 만든다
# 반복문을 만든다
# 반복문에 나온 결과값을 리스트에 추가시킨다
# 함수의 리턴값에 추가된 리스트를 불러온다

#1
def gugudan(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i = i + 1
    return result
print(gugudan(2))

#2
city_name = ["서울", "인천", "대구", "부산", "춘천", "대전"]


def station(city_name):
    result = []
    for name in city_name:
        result.append(name)
    return result
print(station(city_name))


cn = input("도시 이름을 써주세요(콤마로 구분): ").split(",")

city_name.append(cn)
print(city_name)
# cn = input("도시 이름을 써주세요(콤마로 구분): ").split(",")
# cn = [x for x in input("도시 이름을 써주세요(입력 구분자: 콤마(,)) :").split(",")]
# cn = input("도시 이름을 써주세요: ")


#3
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
print(result)

#4
city_name = ["서울", "인천", "대구", "부산", "춘천", "대전"]
for name in city_name:
    print(str(name)+"역입니다.")
else:
    print('Finish')

city_name.append("경주")
