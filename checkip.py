import urllib2
import re


request = urllib2.urlopen('http://checkip.dyndns.org')
web = request.read()

web2 = re.findall(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}",web)


print "THE IP ADDRESS IS :",web2
