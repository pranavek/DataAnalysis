#author: @pranavek


import pymysql.cursors
import pymysql

con = pymysql.connect(host="localhost",user="root",password="****",db="database_name",cursorclass=pymysql.cursors.DictCursor)

with con.cursor() as cursor:
    cursor.execute("show tables;")
    tables = cursor.fetchall()
    cusror.close()

with con.cursor() as cursor:
    for table in tables:
        table_name = table['Tables_in_database_name']
        cursor.execute("desc %s;"%(table_name))
        columns = cursor.fetchall()
        print("\nTable %s"%(table_name))
        for column in columns:
            print(":%s,"%(column['Field']),end=" ")
    cusror.close()
