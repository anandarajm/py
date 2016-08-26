
startport = 28
startlag = 38
description = "CephXD-"
portcount = 3
porttype = "TenG"

if porttype is "TenG":
	incr = 1
else:
	incr = 4
	

for i in range (0,portcount):
	print "interface %s 0/%d" %(porttype,startport)
	print "description %s%d" %(description,(i+1))
	print "port-channel-protocol LACP"
	print "port-channel %d mode active" %(i+startlag)
	print "interface port-channel %d" %(i+startlag)
	print "description %s%d" % (description, (i + 1))
	print "switchport \nvlt-peer-lag port-channel %d" %(i+startlag)
	startport=startport+incr

