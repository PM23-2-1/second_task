import pymysql.cursors

try:
    conn = pymysql.connect(host='localhost',
                             user='111',
                             password='323',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
except pymysql.err.MySQLError as e:
    print(e)