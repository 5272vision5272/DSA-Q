class Node:             ## using as a datastructure having 2 data one for data and the address of next node
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Linkedlist:      ##using as a wrapper class around the node class to implement linked list 
    def __init__(self,data=None):
        self.head = Node(data)
        self.tail = self.head
        self.length = 1

    def append(self,data):  ## apending to the end of the liked list in O(1) because we are using tail value
        newnode = Node(data)
        self.tail.next = newnode
        self.tail = newnode
        self.length+=1
        self.display()
        print()

    def display(self):  ##just display the linked list 
        cur = self.head
        while cur != None:
            print(cur.data,end='-->')
            cur = cur.next

    def prepend(self,data):   ##adding new node next to head
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        self.length+=1
        self.display()
        print()
        
    def insert(self,data,indx): #insert at any index
        if indx == 0:
            self.prepend(data)
        
        elif indx >=self.length:
            print("ERR code indx out of bound")
            return 
        elif indx == self.length-1:
            self.append(data)
        else:
            total = 0
            newnode = Node(data)
            cur = self.head
            while total !=indx-1:  ## traversing to given index-1 and adding new node in between
                cur = cur.next
                total+=1
            newnode.next = cur.next
            cur.next = newnode
            self.length+=1
            self.display()

    def remove(self,indx):
        if indx == 0:  ## just shifing head to head next value 
            self.head = self.head.next
            self.length-=1
            self.display()

        elif indx == self.length-1:  ##traversing to the end of linked list and asigning prev to none 
            cur = self.head
            while cur.next != None:
                pre = cur
                cur = cur.next
            pre.next = None
            self.length-=1
            self.display()

        else:           ##saving pre node and cheching for next 2 node two replace the next node after given index
            cur = self.head
            for i in range(indx):
                pre = cur
                cur = cur.next
                af = cur.next

            pre.next = af
            self.display()



daat = Linkedlist(100)

daat.append(1)
daat.append(12)
daat.append(200)
daat.prepend(-1)
print()
daat.insert(192, 3)
print("remove")
daat.remove(2)
print("length :"+str(daat.length))

    
