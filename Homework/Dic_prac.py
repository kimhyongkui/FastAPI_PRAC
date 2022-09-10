from fastapi import FastAPI

app = FastAPI

# 1. Dict 형식인 변수 생성
# 2. Dict 형식에 맞게 데이터를 저장
# 3. Dict 형식에 맞춰 전체 데이터, 일부 데이터 출력해보기
# 4. Tuple 형식 알아보기

movie = {"공조": [530000, 1],
         "육사오": [76000, 2],
         "헌트": [23000, 3],
         "한산": [11000, 4]}

# 일부 데이터 출력
print(movie["공조"][0], "명", ",", movie["공조"][1], "등", sep="")


# 전체 데이터 출력
for 영화 in movie.keys():
    print(영화, ":", movie[영화])

for 영화 in movie.keys():
    print("영화제목:", 영화, ",", "관객수&순위:", movie[영화])

for 영화, value in movie.items():
    print(영화, ":", value)

def movies():
    for 영화, value in movie.items():
        print("영화제목: {}, 관객수&순위: {}".format(영화, value))
movies()
