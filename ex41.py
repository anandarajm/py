import random
from urllib import urlopen
import sys

word_url = "http://learncodethehardway.org/words.txt"
words = []

phrases = {
    "class aaa(aaa):":
        "Make a class named aaa that is-a aaa.",
    "class aaa(object):\n\tdef __init__(self, bbb)" :
      "class aaa has-a __init__ that takes self and bbb parameters.",
    "class aaa(object):\n\tdef bbb(self, ccc)":
      "class aaa has-a function named bbb that takes self and ccc parameters.",
    "bbb = aaa()":
      "Set bbb to an instance of class aaa.",
    "bbb.bbb(ccc)":
      "From bbb get the bbb function, and call it with parameters self, ccc.",
    "bbb.bbb = 'bbb'":
      "From bbb get the bbb attribute and set it to 'bbb'."
}

if len(sys.argv) == 2 and sys.argv[1]=='english':
    pharse_first=True
else:
    phrase_first=False

for word in urlopen(word_url).readlines():
    words.append(word.strip())

def convert(snippet,phrase):
    class_names=[w.capitalize() for w in
                 random.sample(words,snippet.count("aaa"))]
    other_names=random.sample(words,snippet.count("bbb"))
    print class_names, other_names
    results=[]
    param_names=[]

    for i in range (0,snippet.count("ccc")):
        param_count=random.randint(1,3)
        param_names.append(', '.join(random.sample(words,param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("aaa", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("bbb", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("ccc", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL-D
try:
    while True:
        snippets = phrases.keys()
        random.shuffle(snippets)
        
        for snippet in snippets:
            phrase = phrases[snippet]
            question, answer = convert(snippet, phrase)
            if pharse_first:
                question, answer = answer, question

            print question

            raw_input("> ")
            print "ANSWER:  %s\n\n" % answer
except EOFError:
    print "\nBye"