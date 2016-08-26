import socket as soc
import urllib2 as ul2

# sock1 = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
# sock1.connect(('www.pythonlearn.com', 80))
# sock1.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

print "pythonlearn website is not allowing regular http calls"

# sock1.connect(('www.py4inf.com', 80))
# sock1.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

sock1 = ul2.urlopen('http://www.py4inf.com/code/romeo.txt')

data = sock1.read()
header = sock1.info()
print data, header

sock1.close()
