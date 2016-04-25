import random, string

class account:
    def __init__(self,name,number,balance):
        self.name = name
        self.number = number
        self.balance = balance
    def trans(self,type,*amount):
        if type == 0:
            print "Total amount in account -", self.balance
        elif type == 1:
            if amount < self.balance:
                print "Not enough balance in account"
            else:
                self.balance= self.balance-amount

holder = []

for i in range(10):
    name=''.join(random.choice(string.lowercase) for x in range(8))
    number = ''.join((str(random.randint(0,9)) for x in range(8)))
    balance = random.randint(100,20160)
    holder.append(account(name,number,balance))

for i in holder:
    print i.name, i.number, i.balance

while True:
    print "Enter the account number by name displayed above"
    cust = raw_input(">>>>>")
    for i in holder:
        if cust == i.name:
            print "Accesing account of %s" %i.name
            cust = i
            wrongcust=0
            break
        else:
            wrongcust=1
    if wrongcust == 1:
        print "Customer name not found"
    else:
        break

while True:
    print "Balance enquiry(0) or withdrawal(1)"
    trans = int(raw_input(">>>>"))
    if trans ==0:
        cust.trans(trans)
    elif trans==1:
        print "Enter amount"
        amt = int(raw_input(">>>>"))
        cust.trans(trans,amt)
    break

