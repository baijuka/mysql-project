import os
import datetime
import pymysql

# Get the username from the Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        rows = [("Mathew", 31, "1990-02-06 23:04:56"),
                ("Singh", 66, "1955-05-09 13:12:45"),
                ("Sam", 45, "1975-09-12 01:01:01")]
        cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
        connection.commit()
finally:
    connection.close()