from numpy import *

arr1 = array ([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(arr1)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

# multidimensional array to one dimensional array
arr2 = arr1.flatten()
print(arr2)

# 2 dimensional to 3 dimensional array
arr1 = array ([
    [1,2,3,6,7,8],
    [4,5,6,2,7,8]
])

# arr3 = arr1.reshape(3,3)
# matrix
m = matrix('1,2,3,6; 4,6,7,8 ; 4,5,6,8')

print(m)