
class ring(object):

    def __init__(self):
        self.shopname="Could be bought in any ring shop"

    def shape(self):
        print "Ring typically wil be round in shape"

class ringtype(ring):

    def __init__(self):
        self.shopname="Any Goldhouse"

    def shape(self):
        print "Gold rings are also round in shape"
        super(ringtype,self).shape()
        print "Gold rings have some additional decoration"


basering = ring()
gold_ring = ringtype()

basering.shape()
gold_ring.shape()

print "*"*80
basering.shape()

'''
print basering.shopname
print gold_ring.shopname
'''



