# //Google Question
# //Given an array = [2,5,1,2,3,5,1,2,4]:
# //It should return 2

# //Given an array = [2,1,1,2,3,5,1,2,4]:
# //It should return 1

# //Given an array = [2,3,4,5]:
# //It should return undefined
def findrecur(arr):
    lookup = dict()
    if len(arr)==0:
        return 'Empty Array'

    else:
        for i in range(len(arr)):
            
            if lookup.get(arr[i]) != None:
                return arr[i]

            else:
                lookup[arr[i]] = i

            print(lookup)

        return 'Unique Char'

print(findrecur([2,1,1,2,3,5,1,2,4])) #O(N)
