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

    #Query
    #with connection.cursor() as cursor:
    #    row = ("Bob", 21, "1990-02-06 23:04:56")
    #    cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s)", row)
    #    connection.commit()

    #with connection.cursor() as cursor:
    #    rows = cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")
    #    connection.commit()

    #with connection.cursor() as cursor:
    #    cursor.executemany("DELETE FROM Friends WHERE name = %s", ["Dave", "Fred"])
    #    connection.commit()

    #with connection.cursor() as cursor:
    #    cursor.execute("DELETE FROM Friends WHERE name IN ('Bob', 'Fred');")
    #    connection.commit()
    
    # with connection.cursor() as cursor:
    #     names = ['Dan', 'Dave']
    #     cursor.execute("DELETE FROM Friends WHERE name IN (%s, %s);", names)
    #     connection.commit()
   
    # with connection.cursor() as cursor:
    #     names = ['Fred', 'Dave']
    #     cursor.execute("DELETE FROM Friends WHERE name IN (%s, %s);", names)
    #     connection.commit()

    with connection.cursor() as cursor:
        list_of_names = ['Fred', 'Dave']
        #Prepare a string w2ith the smqe number of placeholders
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name IN ({});".format(format_strings), list_of_names)
        connection.commit()

finally:
    #Close the connection, regardless of whther the above was successful.
    connection.close()
