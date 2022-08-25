import pymysql

def db_connector(sql_command):
    MYSQL_DB = {
        'user'     : 'dbuser',
        'password' : 'abcd1234',
        'host'     : 'localhost',
        'port'     : '3306',
        'database' : 'dino'
    }
    db = pymysql.connect(
        host=MYSQL_DB['host'],
        port=int(MYSQL_DB['port']),
        user=MYSQL_DB['user'],
        passwd=MYSQL_DB['password'],
        db=MYSQL_DB['database'],
        charset='utf8'
    )
    cursor = db.cursor()
    cursor.execute(sql_command)
    result = cursor.fetchall()
    db.commit()
    db.close()
    return str(result).replace("(", "").replace(")", "").replace("'", "").replace(',', '').rstrip()