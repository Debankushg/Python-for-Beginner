#
# def square(a):
#     return a*a

f = lambda a : a*a
result = f(5)
print("Square is " ,result)

#############################################################
#Filter map Reduce

def is_even(n):
    return n%2==0

nums = [3,2,6,8,4,6,2,9]

evens = list(filter(is_even,nums))

print(evens)
###########################################################################

nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda n :  n%2==0 ,nums))

doubles = list(map(lambda n: n*2,evens))
print(doubles)

sum =  reduce(lambda a,b : a+b ,doubles)

print(evens)
print(sum)

