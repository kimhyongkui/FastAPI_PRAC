
# 제목, 관객수 입력
def Input(a, b):
    a, b = input("제목, 관객수 순서로 입력(콤마로 구분): ").split(",")
    return a, b
a = "제목"
b = "관객수"
print(Input(a, b))


# 반복
name = a
aud = b

def add(count):
    dict_movie = []
    for i in range(1, count + 1, 1):
        print("=====추가중======")
        dict_movie.append({'제목': a, '관객수': b})
        if i == count:
            finish = int(input('1번은 딕셔너리 요소 추가 계속, 2번은 종료 : '))
            if finish != 1:
                print("===== 딕셔너리 요소 추가 끝 =====")

