# variable substitution in string printing

roger_slam  = 17
nadal_slam  = 13
novak_slam  = 10
start_year  = 2003
end_year    = 2015
total_slam  = (end_year - start_year) * 4.0
slam_won    = roger_slam+nadal_slam+novak_slam
dominance   = slam_won/total_slam * 100
dom_peryear = 4.0 * slam_won/total_slam


print "between 2003 and 2015 total grandslam titles are %d \n\n" %total_slam 

print "among roger/nadal and novak they have %d grandslam titles\n" %slam_won

print "so these three has dominated the tennis world %f" %dominance, "% of the time between 2003 and 2015" 

print "it is utter domination of these 3 winning atleast %f grand slams each year" %dom_peryear

print "Roger federer - %d \nRafael nadal - %d \nNovak Djokovic - %d " %(roger_slam, nadal_slam, novak_slam)

print "Total slams won by these three dominant players of the last decade = %r" %(roger_slam+nadal_slam+novak_slam)


