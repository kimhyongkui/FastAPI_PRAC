
from fastapi import FastAPI

app = FastAPI()

#3 형변환 연습
city_name = []

def station(city_name1):
    if len(city_name1) > 0:
        city_name1.clear()
    cn = input("도시 이름을 써주세요(콤마로 구분): ").split(",")
    for n in cn:
        n = n.strip()
        city_name1.append(n)
    return city_name1

print(station(city_name), type(city_name))