import requests
requests.packages.urllib3.disable_warnings()

def decorate(desc):
    print "*"*80
    print ">>>>>>", desc
    print "*"*80

def extract(string,key):
    scope = scopewithdupe = []
    string = string.split('>')
    for tag in string:
        if tag.startswith(key):
            scopes = tag.split('<')
            x = str(scopes[0])
            scopewithdupe.append(x)
    scope = list(set(scopewithdupe))
    return scope



basic = ('admin','dellnfv')
xml = """<?xml version="1.0" encoding="UTF-8"?>"""
head = {'Content-type': 'application/xml'}

tzone       = 'https://172.16.105.26/api/2.0/vdn/scopes'
logicalsw   = 'https://172.16.105.26/api/2.0/vdn/scopes/vdnscope-1/virtualwires'


decorate("Get the available transport zone information")

r = requests.get(tzone, auth=basic, verify=False)
zones = extract(r.text,'vdn')
print zones

decorate("Get the available Logical Switch information")
r = requests.get(logicalsw, auth=basic, verify=False)
lswitch = extract(r.text,'virtualwire')
lswitch.sort()
print lswitch

virtualwire = []
restcreatelsw = 'https://172.16.105.26/api/2.0/vdn/scopes/vdnscope-1/virtualwires'

for i in range(1):
    lswname = 'PyRest'+str(i)
    reqXML = '''
    <virtualWireCreateSpec>
    <name>'''+lswname+'''</name>
    <description>Created through Python Requests</description>
    <tenantId>virtual wire tenant</tenantId>
    <guestVlanAllowed>true</guestVlanAllowed>=
    </virtualWireCreateSpec>
    '''

    r = requests.post(restcreatelsw,auth=basic, data=reqXML, headers=head, verify=False)
    unicodevirtualwire = r.text
    x = str(unicodevirtualwire)
    virtualwire.append(x)



startvlan = 10

for i in virtualwire:
    hwvtep = 'https://172.16.105.26/api/2.0/vdn/virtualwires/'+i+'/hardwaregateways'
    for j in range(1,5):
        reqXML = '''
        <hardwaregatewaybinding>
        <hardwareGatewayId>torgateway-20</hardwareGatewayId>
        <vlan>'''+str(startvlan)+'''</vlan>
        <switchName>172.16.101.200</switchName>
        <portName>Te 1/50/'''+str(j)+'''</portName>
        </hardwaregatewaybinding>
        '''
        r = requests.post(hwvtep,auth=basic, data=reqXML, headers=head, verify=False)
    startvlan+=1





