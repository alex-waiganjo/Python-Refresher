thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))
print(type(thistuple))

# Tuple constructor
tuple_items = tuple(("apple", "banana", "cherry"))
print(tuple_items)

# Accesing items by index
print(tuple_items[0])
print(tuple_items[-1])
print(tuple_items[1:])
for item in range(len(tuple_items)):
    print(tuple_items[item])


# Update tuple
p = list(tuple_items)
p[0] = 'mango'
tuples = p
print(tuples)

# Append items
names = ('kelvin', 'mercy', 'rose', 'jane')
add = list(names)
add.append('alex')
names = add
print(names)

# Remove Items
delete_item = list(names)
delete_item.pop()
names = tuple(delete_item)
print(names)

# Unpacking Tuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

add_fruits = list(fruits)
add_fruits.append("strawberry")
add_fruits.append("raspberry")
fruits = tuple(add_fruits)

(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)


# Loop through elements
for items in fruits:
    print(items)

for itemss in range(len(fruits)):
    print(f'Looped by index [{fruits[itemss]}]')
