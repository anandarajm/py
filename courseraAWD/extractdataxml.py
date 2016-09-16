import urllib2 as ul2
import xml.etree.ElementTree as ET

webaddr = ul2.Request('http://python-data.dr-chuck.net/comments_312155.xml')
openconn = ul2.urlopen(webaddr)

data = openconn.read()

tree = ET.fromstring(data)
var = tree.findall('comments')
# count = []
# for name in var[0].findall('comment'):
#     count.append(int(name.find('count').text))
#
# print sum(count)

x = []
c = tree.findall('.//count')

for e in c:
    x.append(int(e.text))
print sum(x)


# Using parse method to extract data from a xml file

# root = ET.parse('xmldata').getroot()
# subroot = root.getchildren()[1]
# # print subroot
# comments = [count for count in subroot.findall('comment')]
#
# countlist = []
# for comment in comments:
#     countlist.append(int(comment.findtext('count')))
#
# # print sum(countlist)