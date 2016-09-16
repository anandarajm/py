import urllib2 as ul2
import json

webaddr = ul2.Request('http://python-data.dr-chuck.net/comments_312159.json')
openconn = ul2.urlopen(webaddr)

data = openconn.read()

parsed_data = json.loads(data)

user_data = parsed_data['comments']
count_list = []
for user in user_data:
    count_list.append(user['count'])
print sum(count_list)