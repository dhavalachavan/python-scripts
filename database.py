#!/usr/bin/python

import MySQLdb
db = MySQLdb.connect("localhost","guest","test123","mysql")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print "Database version : %s " % data
db.close


