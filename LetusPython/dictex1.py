__author__ = 'anandraj'

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']

print inventory['pocket']

inventory['backpack'].sort()

print inventory['backpack']

inventory['backpack'].remove('dagger')

print inventory['backpack']

inventory['gold']=inventory['gold']+50

print inventory['gold']