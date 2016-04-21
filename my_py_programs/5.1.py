n = 0
sum = 0
while True :
    inp = raw_input ('Enter a number:')
    if inp == 'done' : break
    elif len(inp)<1 : continue
    else :
        try :
            num = float(inp)
        except :
            print "Please enter a number"
            continue
        sum = sum + num
        n = n + 1
avg = sum / n

print n, sum , avg
            