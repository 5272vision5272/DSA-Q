# def comm(arr1, arr2):
#     len1 = len(arr1)
#     len2 = len(arr2)

#     flag = False

#     for i in arr1:
#         for j in arr2:
#             if i == j:
#                 return True

#     return flag


# arr1 = [1, 2, 3, 4, 5]
# arr2 = [5, 6, 7]

# print(comm(arr1, arr2))  # O(n^2)

# comman in two array in O(a+b) complexity

def common2(arr1,arr2):
    newd = dict()
    for i in arr1:
        newd[i]=True

    for j in arr2:
        if newd.get(j):
            return "found comman element {}".format(j)

    return "Not found"


arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 5]
print(common2(arr1, arr2))

# O(a+b)
