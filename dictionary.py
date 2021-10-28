d1 = {}
print(type(d1))
d2 = {"harry" : "Burger",
      "Rohan" : "Fish" ,
      "Skill" : "Roti",
      "Subham" : {"B" : "MAGGIE", "L" : "roti" , "D" : "Chicken"}}

print(d2["Subham"],["B"])
d2["Ankit"] = "Junk Food"
d2[420] = "kabab"
del d2["Rohan"]
d3 = d2.copy()
print(d2)
print(d2.get("harry"))
d2.update({"Leena" : "Toffee"})

print(d2.keys())
print(d2.items())

'''
Method	Description

clear()	  Removes all the elements from the dictionary
copy()	   Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	  Returns the value of the specified key
items()	  Returns a list containing a tuple for each key value pair
keys()	  Returns a list containing the dictionary's keys
pop()	   Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	  Updates the dictionary with the specified key-value pairs
values()	  Returns a list of all the values in the dictionary
'''