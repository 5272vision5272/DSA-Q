# def mergearr(arr1,arr2):
#     arrf = arr1 + arr2
#     return sorted(arrf)

# print(mergearr([1,2,6,9], [3,5,10,11])) #complexity of O(NlogN)


# below code can be done in O(N)
def mergearr(arr1,arr2):

    l1 = len(arr1)
    l2 = len(arr2)
    finalarray = list()

    if l1 == 0:
        return arr2

    elif l2 == 0:
        return arr1

    i = 0
    j = 0
    itarr1 = arr1[i]
    itarr2 = arr2[j]

    while (i < l1) and (j < l2) :
        if arr1[i] < arr2[j]:
            finalarray.append(arr1[i])
            i+=1

        else:
            finalarray.append(arr2[j])
            j+=1

    if i < l1 :
        for i in range(l1):
            finalarray.append(arr1[i])

    elif j < l2:
        for j in range(l2):
            finalarray.append(arr2[j]) 

    return finalarray

print(mergearr([], [3,5,10,11]))
