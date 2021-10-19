import array as arr
a = arr.array('i', [1, 3, 5, 7, 9])
print(a[2])

# finding the length of array
a = arr.array('d', [1, 3, 5, 7, 9,12,10,13])
print(len(a))

# Adding an Element
a = arr.array('d',[1, 3, 5, 7, 9])
a.append(13.2)
print(a)
a.extend([9,3,1,2,5])
print(a)
a.insert(2,14)
print(a)

# Removing element of an array
a = arr.array('i',[1, 3, 5, 7, 9])
a.pop()
print(a)
a.pop(2)
print(a)
a = arr.array('i',[1, 3, 5, 7, 9])
a.remove(5)
print(a)

# Concatenation of Array
a = arr.array('d',[1.2, 2.3, 4.5, 1.7, 3.9])
b = arr.array('d',[3.8,4.7,8.6])
# c = arr.array('d')
c = a+b
print('Array c is:  ',c)

# Slicing an array
a = arr.array('d',[1.2, 2.3, 4.5, 1.7, 3.9])
print(a[0:4])
print(a[::-1])

# looping of array
a = arr.array('d',[1.2, 2.3, 4.5, 1.7, 3.9])
print('all values')
for x in a[0:-1]:
	print(x)

# while loop
a = arr.array('i',[12, 2, 4, 1, 3])
b=0
while b<len(a):
	print(a[b])
	b=b+1