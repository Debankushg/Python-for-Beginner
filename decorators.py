def div(a,b):
    if a<b:
        a,b = b,a
    print(a/b)

div(5,4)
#############################################################################

def div(a,b):
    print(a/b)

def smart_div(func):

     def Inner(a,b):
         if a < b:
             a, b = b, a
         return func(a,b)

     return

div = smart_div(div)
div(5,2)