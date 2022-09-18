from fastapi import FastAPI

app = FastAPI

# 1. Dict 형식인 변수 생성
# 2. Dict 형식에 맞게 데이터를 저장
# 3. Dict 형식에 맞춰 전체 데이터, 일부 데이터 출력해보기
# 4. Tuple 형식 알아보기

# movie = {"공조": [530000, 1],
#          "육사오": [76000, 2],
#          "헌트": [23000, 3],
#          "한산": [11000, 4]}
#
# # 일부 데이터 출력
# print(movie["공조"][0], "명", ",", movie["공조"][1], "등", sep="")
#
#
# # 전체 데이터 출력
# for 영화 in movie.keys():
#     print(영화, ":", movie[영화])
#
# for 영화 in movie.keys():
#     print("영화제목:", 영화, ",", "관객수&순위:", movie[영화])
#
# for 영화, value in movie.items():
#     print(영화, ":", value)
#
# movie = []
# for i in range(0,3):
#     name = input('제목: ')
#     aud = input('관객수: ')
#     rank = input('랭킹: ')
#     movie.append({'name': name, 'aud': aud, 'rank': rank})
# print(movie)

#1 수정전
dict_movie = []
while True:
    sel = int(input('1번은 딕셔너리 생성 계속, 2번은 종료 : '))
    if sel == 1:
        print("=====추가중======")
        my_dict = []
        while True:
            name = input('제목: ')
            aud = input('관객수: ')
            rank = input('랭킹: ')
            my_dict.append({'제목': name, '관객수': aud, '랭킹': rank})
            finish = int(input('1번은 딕셔너리 요소 추가 계속, 2번은 종료 : '))
            if finish == 2:
                print("===== 딕셔너리 요소 추가 끝 =====")
                break
        dict_movie.append(my_dict)
    elif sel == 2:
        print("종료합니다.")
        break
    else:
        print("잘못 선택하셨습니다.")
        break
print("내가 만든 영화 순위표 :", dict_movie)

#2 수정후
dict_movie = []
while True:
    sel = int(input('1번은 딕셔너리 생성 계속, 2번은 종료 : '))
    if sel == 1:
        print("=====추가중======")
        my_dict = []
        while True:
            name = input('제목: ')
            aud = input('관객수: ')
            rank = input('랭킹: ')
            my_dict.append({'제목': name, '관객수': aud, '랭킹': rank})
            finish = int(input('1번은 딕셔너리 요소 추가 계속, 2번은 종료 : '))
            if finish == 2:
                print("===== 딕셔너리 요소 추가 끝 =====")
                break
        dict_movie.append(my_dict)
    elif sel == 2:
        print("종료합니다.")
        break
    else:
        print("잘못 선택하셨습니다.")
        break
print("내가 만든 영화 순위표 :", dict_movie)