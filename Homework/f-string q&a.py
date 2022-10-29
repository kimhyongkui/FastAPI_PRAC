# 이걸
for index in range(10):
    product_code = 215673140 + index + 1
    sql = """INSERT INTO product VALUES(
    '""" + str(product_code) + """', '스위트바니 여름신상5900원~롱원피스티셔츠/긴팔/반팔', 23000, 6900, 70, 'F'); """
    print(sql)
    cursor.execute(sql)

# f-string을 사용해서 바꿔보자
title_varchar = title
ori_price = op
discount_price = dp
discount_percent = percent
delivery_varchar =

for index in range(10)
    product_code = 215673140 + index + 1
    sql = """INSERT INTO product VALUES(
    '""" + str(product_code) + """', f'{title},{op},{dp},{percent},{dv}); """