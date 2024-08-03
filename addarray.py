from numpy import *

arr1 = array([1, 2, 3, 4, 5])
arr2 = array([5, 6, 7, 8, 9])
arr3 = array([])

for i in arr1:
        for j in arr2:
                k=i+j
                arr3.append(k)
print(arr3)
