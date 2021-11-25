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
        rows = [("Dave", 22, "1989-02-06 23:04:56"),
                ("Dan", 60, "1962-10-07 01:42:00"),
                ("Fred", 100, "1921-11-20 14:24:30")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        connection.commit()
finally:
    #Close the connection, regardless of whther the above was successful.
    connection.close()
