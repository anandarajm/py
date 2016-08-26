states = {
    'Tamilnadu': 'TN',
    'Andrapradesh': 'AP',
    'Kerala': 'KL',
    'Karnataka': 'KA',
    'Madyapradesh': 'MP'
}

capital = dict(TN='Chennai', AP='Amaravati', KL='Thiruvanandapuram')

capital['KA'] = 'Bangalore'
capital['MP'] = 'Bhopal'

print '*'*80
print "Capital of MP is", capital['MP']
print '*'*80
print "Short form of Kerala is", states['Kerala']
print '*'*80
print "Capital city of Tamilnadu is", capital[states['Tamilnadu']]
print '*'*80
for state, abb in states.items():
    print "Abbreviation of %s is %s" %(state,abb)
print '*'*80
for state, abb in states.items():
    print "%s is abbreviated as %s and its captial city is %s" %(state,abb,capital[abb])
print '*'*80
state = states.get('California')
if state is None:
    print "The database doesnt have California"

city = capital.get('sydney',"Does not exist")
print "Safely getting a non-existent city from dictonary", city
