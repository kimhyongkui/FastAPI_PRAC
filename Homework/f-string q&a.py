# 이걸
for index in range(10):
    product_code = 215673140 + index + 1
    sql = """INSERT INTO product VALUES(
    '""" + str(product_code) + """', '스위트바니 여름신상5900원~롱원피스티셔츠/긴팔/반팔', 23000, 6900, 70, 'F'); """
    print(sql)
    cursor.execute(sql)

# f-string을 사용해서 바꿔보자
item = '스위트바니 여름신상5900원~롱원피스티셔츠/긴팔/반팔'
op = 23000
dp = 6900
dv = 70
pk = 'f'
for index in range(10)
    product_code = 215673140 + index + 1
    sql = """INSERT INTO product VALUES(
    '""" + str(product_code) + """', f'{item},{op},{dp},{dv},{pk}); """