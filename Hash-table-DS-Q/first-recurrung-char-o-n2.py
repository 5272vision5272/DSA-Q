# //Google Question
# //Given an array = [2,5,1,2,3,5,1,2,4]:
# //It should return 2

# //Given an array = [2,1,1,2,3,5,1,2,4]:
# //It should return 1

# //Given an array = [2,3,4,5]:
# //It should return undefined
def findchar(arr):
    if len(arr) == 0:
        return 'Empty Array'

    else:
        for i in range(1,len(arr)):
            for j in range(0,i):  #look back for the same element
                if arr[i] == arr[j]:
                    return arr[i]

        return 'Unique chars'

print(findchar([2,1,1,2,3,5,1,2,4]))