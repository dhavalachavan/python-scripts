#!/usr/bin/python

fo = open("/var/log/syslog","r")

for f in fo:
    f_split =f.split()
    print f_split
    f_list = f_split[0],f_split[1],f_split[2]
    print f_list
