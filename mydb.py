#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '369369'
	)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create database
cursorObject.execute("CREATE DATABASE cafco")

print("All Done! (mydb.py)")
