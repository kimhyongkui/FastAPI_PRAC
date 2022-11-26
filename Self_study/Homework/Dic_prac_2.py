from fastapi import FastAPI
from operator import itemgetter


app = FastAPI

# 4 함수로 만들기

dict_movie = []
name, aud = input

# 반복할 횟수를 고르는 함수
def count1():
    count = int(input('반복할 횟수를 입력하세요: '))
    if count > 0:
        add(count)
    else:
        ask = input('종료를 원하면 yes, 아니면 no를 입력하세요: ')
        if ask == 'yes':
            print("종료합니다.")
        else:
            count1()

# 추가하는 함수
def add(count):
    for i in range(1, count + 1, 1):
        print("=====추가중======")
        name, aud = input("제목, 관객수 순서로 입력(콤마로 구분): ").split(",")
        dict_movie.append({'제목': name, '관객수': aud})
        if i == count:
            finish = int(input('1번은 딕셔너리 요소 추가 계속, 2번은 종료 : '))
            if finish != 1:
                print("===== 딕셔너리 요소 추가 끝 =====")

# 순위 매기는 함수
def count():
    result = sorted(dict_movie, key=itemgetter('관객수'))
    return result


# print("내가 만든 영화 순위표 :", *dict_movie, sep='\n')  #리스트 이름 앞에 "*"붙이면 괄호 생략함

print(count1())
print(dict_movie, sep='\n')
print(result)