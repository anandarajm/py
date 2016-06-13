import os

files =  os.listdir('/home/anandaraj/Scripts/py/courseraDSA')

for f in files:
    # print os.path.join('/home/anandaraj/Scripts/py/courseraDSA',f)
    m = os.path.join('/home/anandaraj/Scripts/py/courseraDSA',f)

for root,dirs,names in os.walk("/home/anandaraj/Scripts/py"):
    for name in names:
        print os.path.join(root,name)
    print '******'
    for name in dirs:
        print ">>>>", os.path.join(root, name)
