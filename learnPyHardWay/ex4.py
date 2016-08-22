# variables and names

roger_slam  = 17
nadal_slam  = 13
novak_slam  = 10
start_year  = 2003
end_year    = 2015
total_slam  = (end_year - start_year) * 4.0
slam_won    = roger_slam+nadal_slam+novak_slam
dominance   = slam_won/total_slam * 100


print "between", start_year, "and", end_year, "total grandslam titles are", total_slam , "\n\n"

print "among roger/nadal and novak they have ", slam_won, "grandslam titles\n"

print "so these three has dominated the tennis world", dominance ,"% of the time between 2003 and 2015"


