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
        if chars == ' ':
            revsent += ' '
        else:
            pos = alphalist.index(chars)
            char = revlist[pos]
            revsent += char
    print revsent


def main():
    try:
        insent = raw_input("Enter string to reverse:")
    except:
        pass
    outsent = answer(insent)

if __name__== "__main__":
    main()