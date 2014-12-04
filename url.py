import urllib2
import re

web = urllib2.urlopen('https://www.facebook.com')

html = web.read()

links = re.findall('''((http|ftp)s?://.*?)''',html)

link = links[0],links[1]

print link
