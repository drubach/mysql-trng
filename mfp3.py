import os 
#import datetime
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
    #with connection.cursor() as cursor:
        #cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'Bob';")
        #connection.commit()

    # with connection.cursor() as cursor:
     #   cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;", 
      #                  (23, "Bob"))
       # connection.commit()

    with connection.cursor() as cursor:
        rows = [(24, "Bob"), (23, "Dave"), (59, "Dan")]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;", 
                        rows)
        connection.commit()
finally:
    #Close the connection, regardless of whther the above was successful.
    connection.close()
