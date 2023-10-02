list1 = ["abc", 34, True, 40, "male"]
print(list1)
print(type(list1))


# Accessing items in a list
print(list1[2:])
print(list1[:3])


# Check if an item exist
list2 = ['kkd', 'jdjd', 'bb']

if 'abc' in list2:
    print("present")
else:
    print('Not in the list')


# Change Items in a list
list2[0] = 'abc'
print(list2)

# Add list items
thislist = ["Apple", "Banana", "Cherry"]
thislist.append('Watermelon')
print(thislist)

# Insert Items
thislist.insert(2, "Guava")
print(thislist)

# Extend lists
thislist2 = ['Mango', 'Lemon', 'Orange', 'Pear']
thislist.extend(thislist2)
print(thislist)
print(thislist[6])

# Remove an item by name
thislist.remove("Mango")
print(thislist)

# Remove an item by index
thislist.pop(5)
thislist.pop()  # Remove the last item
del thislist[3]
# del thislist  #Delete the whole list

# thislist.clear() #Clear items in the list
print(thislist)


# Loop through items in the list

# For loop
for item in range(len(thislist)):
    print(thislist[item])

# List comprehension
print("List comprehension>>")
[print(x) for x in thislist]


# Sorting items
names = ['Alex', 'James', 'Rose', 'Amos', 'Jane', 'Zarika']
nums = [100, 50, 65, 82, 23]
names.sort()
nums.sort()
print(names)
print(nums)

# Sort by reverse order
names.sort(reverse=True)
nums.sort(reverse=True)
print(names)
print(nums)

# Reverse order
names.reverse()
print(names)

# Copy the list items to another variable
name = names.copy()
print(name)
