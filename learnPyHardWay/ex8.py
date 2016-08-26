formatter = "%r %r %r"

print formatter %(34 , 55 , 'ff')
print formatter %('thirty', 'tuesday', 'abc')
print formatter %(True , False , True)
print formatter %(formatter , formatter , formatter)
print formatter %('two words', 'three words', 'string of words using %r')

