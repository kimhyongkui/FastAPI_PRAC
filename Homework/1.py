from fastapi import FastAPI

app = FastAPI()

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

