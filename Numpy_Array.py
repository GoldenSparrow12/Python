from numpy import *

arr = arange(1, 10)
print(arr)

# a = resize(arr, (3, 5))
# print(a)
#
# a = arange(0, 9).reshape(3, 3)
# print(a)
#
# a = append(arr, [4, 5])
# print(a)
#
# A = insert(a, 2, 22)
# print(A)

arr1 = arange(9).reshape(3,3)
arr2 = arange(12).reshape(3,4)
arr3 = arange(9).reshape(3,3)
# print(concatenate((arr1,arr3)))

print(dot(arr1,arr2))
