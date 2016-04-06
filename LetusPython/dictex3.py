__author__ = 'anandraj'

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):
    total = 0
    for item in food:
        if stock[item]>0:
            total = prices[item]+total
            stock[item]= stock[item]-1
    return total

if __name__ == '__main__':
    food = ['banana', 'pear', 'banana', 'apple' , 'banana', 'orange']
    food+= 12*['banana']
    print food
    money = compute_bill(food)
    print "Total money needed %d" %money
    print stock
