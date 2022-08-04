class Node:
    def __init__(self,value=None):
        self.value = value
        self.next=None

class Slist:
    def __init__(self):
        self.headnode=None

    def printlsit(self):
        printval=self.headnode
        while printval is not None:
            print(printval.value,end='-->')
            printval=printval.next
    
    def Atbegin(self,newval):
        Newnode=Node(newval)
    
        Newnode.next=self.headnode
        self.headnode=Newnode


ls=Slist()
ls.headnode = Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
ls.headnode.next=e2
e2.next=e3
e4=Node("Thu")
e3.next=e4

ls.printlsit()
print()
ls.Atbegin("SUN")
ls.printlsit()