import urllib2
import json

print '-'*30
print'This is the most popular video on Youtube'
r = urllib2.urlopen("http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?v=2&alt=jsonc")
web = r.read()
data = json.loads(web)

for item in data['data']['items']:

 print"Video Title: %s" %(item['title'])
 print"Video Category: %s" %(item['category'])


