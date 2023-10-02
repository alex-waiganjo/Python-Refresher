# Arbitrary Arguments, *args
def names(*name):
    print(f'{name[0]} ,{name[1]} ,{name[2]}')

names('Kelvin', 'Jose', 'Grace')


# Passing an argument in the parameter section
def listk(namer='alex'):
    return f'{namer}'

print(listk())


# Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results")
tri_recursion(6)











