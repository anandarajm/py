def answer(s):
    import string
    alphabets = string.lowercase[:]
    alphalist = []
    revlist = []
    for alpha in alphabets:
        alphalist.append(alpha)
        revlist.append(alpha)
    revlist.reverse()
    sentence = 'xyz'
    revsent = str()

    for chars in s:
        if chars not in revlist:
            revsent += chars
        else:
            pos = alphalist.index(chars)
            char = revlist[pos]
            revsent += char
    return revsent


def main():
    try:
        insent = raw_input("Enter string to reverse:")
    except:
        pass
    outsent = answer(insent)
    print outsent

if __name__== "__main__":
    main()
