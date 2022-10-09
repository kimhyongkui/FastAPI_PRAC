import pymysql

#접속(데이터베이스와 연동)
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000', db='prac', charset='utf8')

#커서 가져오기 (SQL문을 실행하거나 실행된 결고라르 돌려받는 통로로 생각하면 됨)
cursor = conn.cursor()

#테이블 만들기
# cursor.execute('sql 내용')
# cursor.fetchall()
# cursor.fetchmany(사이즈)
# cursor.fetchone()

#SQL 구문만들기 (CRUD SQL 구문 등)
# sql = '''
#     CREATE TABLE product (
#         PRODUCT_CODE VARCHAR(20) NOT NULL,
#         TITLE VARCHAR(200) NOT NULL,
#         ORI_PRICE INT,
#         DISCOUNT_PRICE INT,
#         DISCOUNT_PERCENT INT,
#         DELIVERY VARCHAR(2),
#         PRIMARY KEY(PRODUCT_CODE)
#     );
# '''
#테이블 생성(삽입)

#데이터 검색(조회)

#데이터 수정

#데이터 삭제

#SQL 구문 실행하기
cursor.execute(sql)


#INSERT, UPDATE, DELETE 구문은 DB에 저장된 데이터의 변화를 주기에 커밋을 꼭 해주어야 DB에 반영된다
conn.commit()

#DB 연결 끊어주기
conn.close()