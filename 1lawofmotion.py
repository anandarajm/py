# Calculate time saved by over speeding. 

from sys import argv

def lawofmotion(d,v):
    #function to calculate time when given displacement and velocity in minutes
    t = d/v*60
    return t

script, dist, rspeed, aspeed = argv

dist=float(dist)
rspeed=float(rspeed)
aspeed=float(aspeed)


road_eta = lawofmotion(dist,rspeed)

print "Time taken to reach 100 miles @ 65 mph %f" %road_eta

actual_eta = lawofmotion(dist,aspeed)

print "Time taken to reach 100 miles @ 72 mph %f" %actual_eta

print "Actual time saved during the journey %f" %(road_eta-actual_eta)


