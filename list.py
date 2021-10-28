grocery = ["Harpic" , 56, "vim bar", 'deodrant', 'Deodrant' , 'lollypop']
print(grocery[5])

numbers = [2,7,9,11,3]
numbers.sort()
numbers.reverse()
print(numbers)
# slicing
print(numbers[1:])
# extended slcing
print(numbers[::-1])
numbers.append(47)
print(numbers)

numbers.insert(3,67)
print(numbers)
numbers.remove(9)
print(numbers)
numbers.pop()
numbers[4] = 97
print(numbers)

# tupple
tp = (1,3,4)
# tp[1] = 46
print(tp)

# swapping of num
a = 24
b = 12
a,b = b,a
print(a,b)

'''
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list 
'''