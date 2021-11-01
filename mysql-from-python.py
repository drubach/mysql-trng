import os 
import pymysql

username = "drubach"

# Connect to database
connection = pymysql.connect(host='LocalHost',
                            user = username,
                            password = '!RmrEJJRy1258',
                            db = 'Chinook')

try:
    #Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        #result = cursor.fetchall()
        for row in cursor:
            print(row)
finally:
    #Close the connection, regardless of whther the above was successful.
    connection.close()
