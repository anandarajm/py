def answer(numlist):
    while sum(numlist)%3:
        if sum(numlist)%3==1:
#            print '1',numlist
            size = len(numlist)
            for n in [1,4,7]:
#               print '>', numlist
                if n in numlist:
                    numlist.remove(n)
#                    print '1st 1 if - ', numlist
                    break
            if len(numlist) == size:
                for n in [2,5,8]:
                    if n in numlist:
                        numlist.remove(n)
#                        print '2nd 1 if - ', numlist
                        break

        elif sum(numlist)%3==2:
            print '2', numlist
            size = len(numlist)
            for n in [2,5,8]:
                print '>', numlist, n
                if n in numlist:
                    numlist.remove(n)
                    print '1st 2 if - ', numlist
                    break
            print size, len(numlist)
            if len(numlist) == size:
                for n in [1, 4, 7]:
                    print '----------> ', n
                    if n in numlist:
                        numlist.remove(n)
                        print '2nd 2 if - ', numlist
                        break


    if len(numlist):
        numlist.sort(reverse=True)
        return listtoint(numlist)
    else:
        return 0

def listtoint(sortlist):
    num = str()
    for elem in sortlist:
        num += str(elem)
    return num


def main():
    try:
        insent = raw_input("Enter the number list:")
        inlist = insent.split(',')
        inlist = [int(a) for a in inlist]
    except:
        pass
    outsent = answer(inlist)
    print outsent

if __name__== "__main__":
    main()