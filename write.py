#!/usr/bin/python

import os

fo= open("hhmm.py",'r+')
str = fo.read(10);
print "",str
position = fo.tell();
print "current position ", position

position = fo.seek(0,0)
print "current position ", position

os.rename("hhmm.py","hhmp.py")
os.mkdir("ram")
os.getcwd()
fo.close()
