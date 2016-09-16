from bs4 import BeautifulSoup as bsoup
import urllib2 as ul2

webaddr = 'http://python-data.dr-chuck.net/known_by_Ainslie.html'

count = 7
position = 17
for i in range(count):
    createurl = ul2.Request(webaddr)
    connecturl = ul2.urlopen(createurl)

    soup = bsoup(connecturl,'html.parser')
    tags = soup('a')
    links = []
    for tag in tags:
        links.append(tag.get('href',None))
    print links[position]
    webaddr = links[position]