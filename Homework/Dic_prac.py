import operator

from fastapi import FastAPI
import re
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

# 1. 수정전
# dict_movie = []
# while True:
#     sel = int(input('1번은 딕셔너리 생성 계속, 2번은 종료 : '))
#     if sel == 1:
#         print("=====추가중======")
#         my_dict = []
#         while True:
#             name = input('제목: ')
#             aud = input('관객수: ')
#             rank = input('랭킹: ')
#             my_dict.append({'제목': name, '관객수': aud, '랭킹': rank})
#             finish = int(input('1번은 딕셔너리 요소 추가 계속, 2번은 종료 : '))
#             if finish == 2:
#                 print("===== 딕셔너리 요소 추가 끝 =====")
#                 break
#         dict_movie.append(my_dict)
#     elif sel == 2:
#         print("종료합니다.")
#         break
#     else:
#         print("잘못 선택하셨습니다.")
#         break
# print("내가 만든 영화 순위표 :", dict_movie)
#
#
# 1. 왜 while이 2번 들어갔는가?
# 2. 굳이 while을 2번 써야하는가?
# 3. Append를 2번 사용했는데 굳이 이렇게 했어야 하는가?
# 4. 딕셔너리를 n번 추가하기 -> n번 입력후 계속 추가할건지 물어보기
#
# 2. 수정후
# dict_movie = []
# while True:
#     count = int(input('반복할 횟수를 입력하세요: '))
#     if count > 0:
#         for i in range(1, count + 1, 1):
#             print("=====추가중======")
#             name = input('제목: ')
#             aud = input('관객수: ')
#             rank = input('랭킹: ')
#             dict_movie.append({'제목': name, '관객수': aud, '랭킹': rank})
#             if i == count:
#                 finish = int(input('1번은 딕셔너리 요소 추가 계속, 2번은 종료 : '))
#                 if finish != 1:
#                     print("===== 딕셔너리 요소 추가 끝 =====")
#                     break
#     elif count == 0:
#         print("종료합니다.")
#         break
#     else:
#         print("잘못 선택하셨습니다.")
#         break
# print("내가 만든 영화 순위표 :", *dict_movie, sep='\n')  #리스트 이름 앞에 "*"붙이면 괄호 생략함
#
# 3. 수정 2번째
tu_movie = []
dic_movie = {}
movie_list = []
tmpTup = None
totalRank, currentRank = 1, 1

while True:
    count = int(input('반복할 횟수를 입력하세요: '))
    if count > 0:
        for i in range(1, count + 1, 1):
            print("=====추가중======")
            name = input('제목: ')
            aud = int(input('관객수: '))
            tu_movie.append((name, aud))
            if i == count:
                finish = int(input('1번은 딕셔너리 요소 추가 계속, 2번은 종료 : '))
                if finish != 1:
                    print("===== 딕셔너리 요소 추가 끝 =====")
                    break
    elif count == 0:
        print("종료합니다.")
        break
    else:
        print("잘못 선택하셨습니다.")
        break

if __name__ == "__main__":
    for tmpTup in tu_movie:
        tName = tmpTup[0]
        tAmount = tmpTup[1]
        if tName in dic_movie:
            dic_movie[tName] += tAmount
        else:
            dic_movie[tName] = tAmount

    print('--------------------')
    print("내가 만든 영화 순위표")
    movie_list = sorted(dic_movie.items(), key=operator.itemgetter(1), reverse=True)
    # .items() : 딕셔너리 변수에만 사용할 수 있고, 튜플 형태로 구분한다
    print(movie_list)
    print('제목  \t관객수\t순위')
    print('--------------------')
    print(movie_list[0][0], '\t', movie_list[0][1], '\t', currentRank)
    for i in range(1, len(movie_list)):
        totalRank += 1
        if movie_list[i][1] == movie_list[i-1][1]:
            pass
        else:
            currentRank = totalRank
        print(movie_list[i][0], '\t', movie_list[i][1], '\t', currentRank)