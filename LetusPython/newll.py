__author__ = 'anandraj'

class node:
    def __init__(self,data,pointer=None):
        self.data = data
        self.pointer = pointer

    def __str__(self):
        return str(self.data)

class linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self,*data):
        if not self.head:
            n=node(data)
            self.head=n
            return
        else:
            n=self.head
            while n.pointer!= None:
                n=n.pointer
            newnode = node(data)
            n.pointer=newnode
            return

    def printlist(self):
        n = self.head
        while n:
            print n , n.pointer
            n=n.pointer

ll = linkedlist()
listelem = [1,3,5,7,9]
for i in listelem:
    ll.append(i)

ll.printlist()