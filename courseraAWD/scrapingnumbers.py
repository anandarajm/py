from bs4 import BeautifulSoup as bsoup
import urllib2 as ul2

webaddr = 'http://python-data.dr-chuck.net/comments_312158.html'

req_data = ul2.Request(webaddr)
connection = ul2.urlopen(req_data)

soup = bsoup(connection,'html.parser')
tags = soup('span')
total = 0
for span in tags:
    span.__dict__
    total = total + int(span.contents[0])

print total