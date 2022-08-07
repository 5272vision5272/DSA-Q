class Arrays :
    def __init__(self):
        self.data = {}
        self.length = 0

    def get(self,index):
        return self.data[index]

    def appends(self,item):
        self.data[self.length] = item
        self.length+=1
        return self.data

    def pop(self):
        poped = self.data[self.length - 1]
        self.data.popitem()
        self.length-=1
        return poped

    def insert(self,ind,itemin):
        self.moveitems(ind)
        self.data[ind]=itemin
        return self.data

    def moveitems(self,indmove):
        for i in range(self.length,indmove-1,-1):
            print(" "+str(i)+" "+str(indmove))
            self.data[i] = self.data[i-1]
        self.length+=1
    

myarray = Arrays()
myarray.appends("Hi")
myarray.appends(",")
myarray.appends("nice")
myarray.appends("to")
print(myarray.data)
myarray.insert(1, "you")
print(myarray.data)
print(myarray.length)

