class house(object):
    def __init__(self):
        self.laptop = "Dell"

    def tv(self, brand):
        print brand


anand = house()
anand.tv("samsung")
print anand.laptop

udhay = house()
udhay.laptop="HP"
print udhay.laptop
udhay.tv("Vizio")

vinoth=house()
vinoth.laptop='MAC'
vinoth.tv('Vizio')

# class aaa(aaa):                     #Make a class named aaa that is-a aaa.",


class aaa(object):
    def __init__(self, bbb):        #class aaa has-a __init__ that takes self and bbb parameters.

class aaa(object):
    def bbb(self, ccc):             #class aaa has-a function named bbb that takes self and ccc parameters.",
bbb = aaa()                        #Set bbb to an instance of class aaa.",
bbb.bbb(ccc)                       #"From bbb get the bbb function, and call it with parameters self, ccc.",
bbb.bbb = 'bbb'                    #"From bbb get the bbb attribute and set it to 'bbb'."
