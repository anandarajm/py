import socket as soc
import urllib2 as ul2

# sock1 = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
# sock1.connect(('www.pythonlearn.com', 80))
# sock1.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

print "pythonlearn website is not allowing regular http calls"

# sock1.connect(('www.py4inf.com', 80))
# sock1.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')


site='http://www.pythonlearn.com/code/intro-short.txt'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = ul2.Request(site,headers=hdr)
page = ul2.urlopen(req)

print page.info()
print page.read()



