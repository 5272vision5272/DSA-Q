class hashtable : 
    def __init__(self,size):
        self.data = [None] * size

    def _hash(self,key) :  #Hash Function let it be O(1)
        hash = 0
        for i in range(0,len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash

    def push(self,key,value):  #push data in hash Function O(1)
        hashadd = self._hash(key)
        if self.data[hashadd] == None:
            self.data[hashadd] = []

        self.data[hashadd].append([key,value])
        return self.data

    def display(self,key):  #lookup in hashtable --> if there is no collision then O(1) if collision is there than O(N)
        hashadd = self._hash(key)

        if not self.data[hashadd]:
            return False

        else:
            pairs = self.data[hashadd]
            for i in range(len(pairs)):
                if pairs[i][0]==key:
                    return pairs[i][1]

            return False


table = hashtable(2)
print(table.push('yes', 10))
print(table.display('yes'))
print(table.push('no', 12))
print(table.display('no'))


