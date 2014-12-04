#!/usr/bin/python

import MySQLdb
db = MySQLdb.connect("localhost","root","dhaval123","mysql")
cursor = db.cursor()
sql = """ CREATE TABLE EMPLOYEE ( FIRST_NAME CHAR(20) NOT NULL,LAST_NAME CHAR(20),AGE INT,SEX CHAR(1),INCOME FLOAT )"""
cursor.execute(sql)
db.close
