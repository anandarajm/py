import urllib as ul2
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    url = serviceurl + ul2.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = ul2.urlopen(url)
    data = uh.read()

    jsondata = json.loads(data)

    print jsondata['results'][0]['place_id']

