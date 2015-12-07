__author__ = 'anandraj'

statement = """thanam tharum kalvi tharum oru naalum thalarvu ariya manam tharum \
    deiva vadivum tharum nenjil vanjam illa inam tharum  nallanavellam tharum \
    anbar enbavarke ganam tharum poonguzhalaal abhiraamiyin kadai kangale"""

def break_words(statment):
    words=statement.split(' ')
    return words

def sort_words(statement):
    words=sorted(statement)
    return words

def first_word(statement):
    print statement.pop(0)

def last_word(statement):
    print statement.pop(-1)

def sort_sentence(statement):
    words=break_words(statement)
    return sort_words(words)

def first_last(statement):
    words=break_words(statement)
    first = first_word(words)
    last = last_word(words)

def sort_first_last(statemnet):
    sorted = sort_sentance(statemnet)
    first = first_word(sorted)
    last = last_word(sorted)

