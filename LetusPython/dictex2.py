__author__ = 'anandraj'

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock={}
stock["banana"]= 6
stock["apple"]= 0
stock["orange"] =32
stock["pear"]= 15

for fruit in prices:
    print fruit,'\n',"price:",prices[fruit],'\n',"stock:",stock[fruit]

total = 0

for fruit in prices:
    money = prices[fruit] * stock[fruit]
    total = total+money

p = prices.values()
s = stock.values()
m= map(lambda x,y: x*y,p,s)
t = reduce(lambda x,y:x+y,m)
print total, t

