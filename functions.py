

def greet():
    print("good morning")

greet()
##################################
def add(x,y):
    c = x+y
    print(c)
add(5,4)
##################################
def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d

r1, r2 = add_sub(42,20)
print(r1,r2)