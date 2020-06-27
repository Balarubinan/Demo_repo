import mysql.connector
from mysql.connector import Error
con=None
cur=None
try:
    con=mysql.connector.connect(host='Balarubinan.mysql.pythonanywhere-services.com',
                                database='Balarubinan$project_database',
                                user='Balarubinan',
                                password='$Hsia#12')
    if con.is_connected():
        info=con.get_server_info()
        print("Db linked")
        cur=con.cursor()
        cur.execute("select database();")
        rec=cur.fetchone()
        print("Youre connnected to databasse",rec)
except Error as e:
    print("Error while trying o connect to the database")
finally:
    if(con.is_connected()):
        cur.close()
        con.close()
        print("DB link cut")