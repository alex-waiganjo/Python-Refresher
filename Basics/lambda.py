# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

b = lambda a  : a * 2
print(b(7))

# Takes in two arguments
b = lambda a ,c : a * c
print(b(7,5))

# Takes in three arguments 
b = lambda a ,c,d : a * c *d
print(b(7,5,4))


# Return lamaba function 
def func(n):
    return lambda anoy: anoy *n

func1 = func(8)
print(func1(4))
