import urllib2 as ul2
from bs4 import BeautifulSoup
from collections import Counter


def find_a_tag(givenurl):
    linksinpage = []
    mag = givenurl
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) '
                         'Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

    req = ul2.Request(mag, headers=hdr)
    content = ul2.urlopen(req)
    soup = BeautifulSoup(content, "html.parser")
    for atag in soup.findAll('a'):
        linksinpage.append(str(atag.get('href', None)))
    return linksinpage

swarajya = find_a_tag('http://www.swarajyamag.com')

dictoflinks = Counter(swarajya)

for k,v in dictoflinks.iteritems():
    if v > 1:
        if k != 'javascript:void(0)':
            print k,v
