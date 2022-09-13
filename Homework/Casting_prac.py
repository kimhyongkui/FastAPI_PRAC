from fastapi import FastAPI

app = FastAPI()

# 형변환 연습
city_name = []

def station(city_name1):
    if len(city_name1) > 0:
        city_name1.clear()
    cn = input("도시 이름을 써주세요(콤마로 구분): ").split(",")
    for n in cn:
        n = n.strip()
        city_name1.append(n)
    return city_name1

print(station(city_name), type(station(city_name)))

# 리스트 -> 딕셔너리
    #1. Dictionary Comprehesion 이용
dictionary = {string : i for i,string in enumerate(city_name)}
print(dictionary, type(dictionary))

dictionary = {string : 0 for string in city_name}
print(dictionary, type(dictionary))

    #2. dict.fromkeys(key,value)이용
dictionary = dict.fromkeys(city_name)
print(dictionary, type(dictionary))

    #3. list의 값을 value로 갖는 dict 만들기
dictionary = {i : city_name[i] for i in range(len(city_name))}
print(dictionary, type(dictionary))

# 리스트 -> 튜플
print(tuple(city_name), type(tuple(city_name)))

# 리스트 -> 문자열
    #1. 반복문으로 리스트의 모든 요소들을 하나의 문자열로
def listtostring(city_name):
    result = ""
    for s in city_name:
        result = result + s + " "
    return result.strip()

result = listtostring((city_name))
print(result, type(result))

    #2. String.join()으로 리스트의 모든 요소들을 하나의 문자열로 변환
result = "_".join(s for s in city_name)
print(result, type(result))

    #3. join()으로 숫자가 포함된 리스트를 문자열로 변환
result = " ".join(str(s) for s in city_name)
print(result, type(result))

    #4. map()으로 숫자가 포함된 리스트를 문자열로 변환
result = " ".join(map(str, city_name))
print(result)

