import os 
import datetime
import pymysql

username = "drubach"

# Connect to database
connection = pymysql.connect(host='LocalHost',
                            user = username,
                            password = '!RmrEJJRy1258',
                            db = 'Chinook')

try:
    #Create a table
    #with connection.cursor() as cursor:
        #cursor.execute("""CREATE TABLE IF NOT EXISTS 
                        #Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not an error) 
        # if the table already exists.

    #Insert into table
    with connection.cursor() as cursor:
        row = ("Bob", 21, "1990-02-06 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
finally:
    #Close the connection, regardless of whther the above was successful.
    connection.close()
