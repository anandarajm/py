__author__ = 'anandraj'

class node:
    def __init__(self,data=None,nodepointer = None):
        self.data = data
        self.nodepointer = nodepointer
    def get_data(self):
        return self.data
    def get_next(self):
        return self.nodepointer
    def set_next(self,pointer):
        self.nodepointer=pointer
    def __str__(self):
        return str(self.data)


# Accessing an object(instance of a class) directly without any method returns its address

class linkedlist:
    def __init__(self,head=None):
        self.head=head

    def insert(self,*data):
        new_node=node(data)
        new_node.set_next(self.head)
        self.head=new_node
        c = self.head
        # print ">>>", c.get_data() , c.get_next() , c


    def printll(self):
        current = self.head
        while current:
            print str(current)
            current = current.set_next(current)

    def size(self):
        current=self.head
        count=0
        while current:
            count+=1
            current = current.get_next()
        return count

    def search(self,data):
        current=self.head
        found=False
        while current and found is False:
            if current.get_data==data:
                found=True
            else:
                current = current.get_next()
        if found is False:
            raise ValueError("data not in list")
        return current


ll = linkedlist()
ll.insert(5)
ll.insert(6)
print ll.size()
print ll.printll()

