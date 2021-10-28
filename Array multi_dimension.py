from numpy import *

arr = array([1,2,3,4,6,5,8.8])
print(arr)
arr = linspace(0,15)
print(arr)
arr = arange(1,15,3)
print(arr)
arr = logspace(1,40,5)
# print(arr.dtype)
print('%.2f' %arr[0])

arr = ones(5,int)
print(arr)

arr = zeros(5,int)
print(arr)