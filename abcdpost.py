#!/usr/bin/python
import smtplib
fromaddr = 'dhavalachavan29@gmail.com'
toaddr = 'hardik.s.shah1987@gmail.com'
msg = 'hi!!'
username = 'dhavalachavan29@gmail.com'
password = 'shivgoogle'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, msg)
server.quit()
