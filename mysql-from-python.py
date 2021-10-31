import os 
import pymysql

username = os.getlogin()

# Connect to database
connection = pymysql.connect(host='LocalHost',
                            user = username,
                            password = '!RmrEJJRy1258',
                            db = 'Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #Close the connection, regardless of whther the above was successful.
    connection.close()
