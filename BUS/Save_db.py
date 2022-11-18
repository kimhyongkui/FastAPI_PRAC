import pymysql
def mysql_save(fest_list):
    conn=pymysql.connect(host='localhost',
                        user='root',
                        password='1234',
                        db='tourproject',
                        charset='utf8')
    cursor=conn.cursor()
    sql="insert into festival(festival_title,festival_addr,usage_day,festival_area,homepage,thumb,traffic,lat,lng) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.executemany(sql,fest_list)
    conn.commit()
    conn.close()
mysql_save(fest_list)

