myset = {"apple", "banana", "cherry", "apple", True,
         1, False, 0}  # Duplicate values are ommitted
print(myset)
print(len(myset))

set1 = {"John", 'Mid-level', True, 25, "Male"}
print(set1)

# Adding items to a list
set1.add('Data Scientist')
print(set1)


# Join two sets
set2 = {"Rose", "Senior", False, 30, "Female"}
set1.update(set2)
print(set1)


# Remove items
set1.remove('Senior')
set1.pop()
set1.discard('Rose')
print(set1)


# Loop through
for items in set1:
    print(items)

# Union
set3 = {"Ken", "Junior", False, 20, "Male"}
joined_sets = set2.union(set3)
print(joined_sets)

# Keep itesms that are present in both sets
x = {"apple", "banana", "cherry", 'google'}
y = {"google", "microsoft", "apple"}

# x.intersection_update(y)
z = x.intersection(y)
print(z)

# Return a new set, that contains only the elements that are NOT present in both sets.
z = x.symmetric_difference(y)
print(z)
