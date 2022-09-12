from fastapi import FastAPI


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
city_name = []

def station(city_name1):
    if len(city_name1) > 0:
        city_name1.clear()
    cn = input("도시 이름을 써주세요(콤마로 구분): ").split(",")
    # print(len(cn)) -> cn의 길이를 확인해보는 거니까 굳이 필요없는듯?
    for n in cn:
        n = n.strip()
        city_name1.append(n)
    return city_name1

print(station(city_name))
station(city_name)
print(city_name)



