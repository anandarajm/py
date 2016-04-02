import argparse

while True:
    try:
        print "Enter any character"
        limit = int(raw_input(">>>"))
        break
    except:
        print "Enter only characters"
        print traceback.format_exc()
        continue

for i in range (2,(limit+1)):
    for p in range (2,i):
        print "*"*40 , i, p
        if i%p == 0:
            break
    else:
        print i
