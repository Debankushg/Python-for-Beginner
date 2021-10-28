
def update(x):
    print(id(a))
    x =8
    print('x = ',x)

a = 10
print(id(a))
update(a)
print('a = ',a)

# Arguments are 4 types
# POSITION, KEYWORD, DEFAULT , VARIABLE LENGTH

# postion Argument
def person(name,age):
    print(name)
    print(age)

person("Navin" , 28)

#KEYWORD argument
def person(name,age):
    print(name)
    print(age-2)

person( age= 28, name = "DEB")

#DEFAULT Argument
def person(name,age = 18):
    print(name)
    print(age)

person( "DUMPY")

# Variable Length Argument
def sum(*b):
    c = 0
    for i in b:
        c = c + i
    print(c)


sum(5,6,7,38)