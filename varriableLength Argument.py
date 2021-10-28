

def person(name ,**data):

    print(name)
    # print(data)
    for i,j in data.items():
        print(i,j)

person('deb' ,age =  28 ,city= 'mumbai' ,mob =9832175)

##### GLOBAL  AND  LOCAL VARRIABLE

a = 10

def something():
    global a
    a = 20

    print("In fun" , a) #local variable
something()


print("Outside" , a)  #Global Varriable

###############################################################################
a = 10
def something():
    a = 9
    x = globals()['a']
    print("In fun" , a) #local variable

    globals()['a'] = 15
something()

print("Outside" , a)  #Global Varriable