import pymysql

db = pymysql.connect(
    user='root',
    password='po919480!@',
    db='bus',
    host='localhost',
    charset='utf8'
)

sql = '''
CREATE TABLE station (
    id int primary key auto_increment not null,
    name varchar(32),
    age int,
    address varchar(32)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
'''

with db.cursor() as cursor:
    cursor.execute(sql)