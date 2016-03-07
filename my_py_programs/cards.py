# Program to fetch a random card from deck of cards

import random

value = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
symbol = ["Spade","Clubs","Diamond","Hearts"]

rand_val = random.randint(0,len(value))
rand_sym = random.randint(0,(len(symbol)-1))

if rand_val is 13:
    print "The random card is a Joker"
else:
    val_is = value[rand_val]
    sym_is = symbol[rand_sym]
    print "The random card is %s %s" %(val_is,sym_is)

print random.choice(value), random.choice(symbol)