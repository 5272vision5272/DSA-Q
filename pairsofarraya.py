from array import array

def pairof(arr1,arr2):
    count=0
    for i in arr1:
        for k in arr2:
            count=count+1
            print("pair {}: {},{}".format(count,i,k))
            print("Sum of Pairs {}: {}".format(count,i+k))
        
arr1=[1,2,3,4,5,6] #length =n
arr2=[9,7,6,0] #length =m

print(len('abhi'))

pairof(arr1, arr2)

#Big O notation : O(n**2) or O(m*n)
