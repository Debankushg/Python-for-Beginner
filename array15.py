from numpy import *

arr1 = array([1,2,3,4,5,6])
arr2 = array([6,5,9,3,4,7])

arr3 = arr1 + arr2
print (arr3)
# different function performed by an array
arr = array([0,4,9,64,5,90])
print(sin(arr))
print(cos(arr))
print(sqrt(arr))
print(concatenate([arr1 , arr2]))

# copying an array
arr1 = array([1,2,3,4,5,6])
arr2 = arr1  #aliasing
print(arr1)
print(arr2)
arr2 = arr1.view()  #shallow coppy
print(arr1)
print(arr2)

arr2 = arr1.copy()  #deep copy
print(arr1)
print(arr2)
print(id(arr1))

