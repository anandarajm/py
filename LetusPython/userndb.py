import getpass

credentials = {'admin':'pass', 'admin1':'pass1'}

credentials['admin2'] = 'pass2'

print credentials['admin2']

print "total number elements in dict credentials ", len(credentials)

for user in credentials:
    print credentials[user]
print credentials
print credentials.items()
print credentials.keys()
print credentials.values()


# print "Enter the password of user admin"
# txt = getpass.getpass()
#
# if txt == credentials['admin']:
#     print "Authentication successful"
# else:
#     print "Wrong password"