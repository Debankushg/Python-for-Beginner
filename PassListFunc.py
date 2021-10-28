
def count(lst):

    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd
lst = [20,45,26,48,75,55,43,28,91]
even , odd = count(lst)

print('Even : {} and Odd : {}'.format(even,odd))
