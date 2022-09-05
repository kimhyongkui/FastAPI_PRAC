def conv_ingredients_to(input_재료_1st, input_재료_2nd):
    ingredient_sets = [['파', '대파', '쪽파'], ['닭', '닭', '치킨', '닭고기', '닭봉'],
                       ['계란', '달걀'],
                       ['면', '우동사리', '파스타면', '소면', '당면', '에그면'],
                       ['버섯', '양송이버섯', '팽이버섯'],
                       ['육수', '콜드브루육수'],
                       # ['고기', '돼지고기', '베이컨', '얇은 돼지고기', '얇은 소고기', '얇은 고기', '폭립',
                       # '다진고기', '간 돼지고기', '튀긴 고기']
                       ]

    ingredient_dict = {}

    for i_set in ingredient_sets:
        for i in i_set:
            ingredient_dict[i] = i_set[0]

        if input_재료_1st in ingredient_dict:
            input_재료_1st = ingredient_dict[input_재료_1st]

        if input_재료_2nd in ingredient_dict:
            input_재료_2nd = ingredient_dict[input_재료_2nd]

    Menu = {"양파덮밥": ['양파', '계란'],
            "순두부찌개": ['두부', '계란', '고기'],
            '고추장파닭': ['파', '닭'],
            "쫄면": ['쫄면', '양배추', '깻잎'],
            '부추리조또': ['부추', '쌀', '육수', '양파'],
            '닭볶음탕': ['닭', '감자', '당근', '우동사리'],
            '폭찹 스테이크': ['돼지고기', '양송이버섯', '파프리카'],
            '국수': ['육수', '소면', '김치', '계란', '만두'],
            '투움바 파스타': ['파스타면', '우유', '케찹', '갓뚜기 야채스프', '새우', '양송이버섯'],
            '콩나물 불고기': ['백선생sty.', '승우아빠sty.'],
            '까르보나라': ['베이컨', '파마산치즈', '계란', '파스타면'],
            '우동볶음': ['우동사리', '베이컨', '양배추'],
            '찜닭': ['당면', '닭', '감자', '양배추'],
            '하이라이스': ['팽이버섯', '양파', '얇은 돼지고기', '하이라이스'],
            '알리오 올리오': ['파스타면', '새우', '마늘', '페페론치노'],
            '등갈비 김치찜': ['돼지고기', '김치', '콜드브루육수'],
            '밀푀유 나베': ['콜드브루육수', '양배추', '깻잎', '얇은 소고기'],
            '칠리새우': ['새우', '감자전분', '기름', '양파'],
            '잡채': ['파프리카', '양파', '버섯', '당면', '청경채', '얇은 고기'],
            '닭날개조림': ['닭', '파'],
            '허니갈릭폭립': ['폭립', '소스', '깻잎', '플레인 시리얼'],
            '탄탄면': ['에그면', '다진고기', '청경채', '소스'],
            '불맛 짬뽕라면': ['너구리', '파', '양배추', '배추', '양파', '얇은 돼지고기', '간 돼지고기'],
            '강식당 라면': ['라면', '양념장', '양배추', '튀긴 고기', '계란'],
            '만능양파볶음': ['양파']
            }

    i = 0
    q = 0

    while (i < len(list(Menu.keys()))):
        if (input_재료_1st and input_재료_2nd) in ((list(Menu.values())[
            i])):  # O O print(len(list(Menu.values())[i]), list(Menu.values())[i], list(Menu.keys())[i])
            global one_ingredient_menu, two_ingredients_menu, three_ingredients_menu, four_ingredients_menu

            if len(list(Menu.values())[i]) == 1:  # input이 메뉴 재료일 때
                one_ingredient_menu.append(list(Menu.keys())[i])

            elif len(list(Menu.values())[i]) == 2:  # input + 재료1개가 재료일
                two_ingredients_menu.append(list(Menu.keys())[i])

            elif len(list(Menu.values())[i]) == 3:  # input + 재료2개
                three_ingredients_menu.appendlist(list(Menu.keys())[i])

            else:  # input + 재료3개이상
                four_ingredients_menu.append(list(Menu.keys())[i])



        elif (input_재료_1st or input_재료_2nd) not in ((list(Menu.values())[i])):
            one_ingredient_menu = 'Does Not Exist'
            two_ingredients_menu = 'Does Not Exist'
            three_ingredients_menu = 'Does Not Exist'
            four_ingredients_menu = 'Does Not Exist'

        else:
            if q < len(list(Menu.values())[i]) - 1:
                q = q + 1
                continue

            else:
                i = i + 1
                q = 0
                continue
        i = i + 1
        q = 0


one_ingredient_menu = []
two_ingredients_menu = []
three_ingredients_menu = []
four_ingredients_menu = []

input_재료_1st = input('Enter 1st ingredient to see Menu available: ')
input_재료_2nd = input('Enter 2nd  ingredient to see Menu available: ')
conv_ingredients_to(input_재료_1st, input_재료_2nd)

print('\n')
print('With only', input_재료_1st, 'and', input_재료_2nd + ':', one_ingredient_menu)
print('With', input_재료_1st, 'and', input_재료_2nd, '+1' + ':', two_ingredients_menu)
print('With', input_재료_1st, 'and', input_재료_2nd, '+2' + ':', three_ingredients_menu)
print('With', input_재료_1st, 'and', input_재료_2nd, '+α' + ':', four_ingredients_menu)



