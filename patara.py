import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("dhavalachavan29@gmail.com", "shivgoogle")


msg = "\nHello!" 
server.sendmail("dhavalachavan29@gmail.com", "hardik.s.shah1987@gmail.com", msg)
