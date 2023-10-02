person = {
    "name": "Abdi Salam",
    "age": 24,
    "profession": "Data Analyst",
    "Location": "Kenya",
    "other": {
        "marital_status": "Dating",
        "height": 5.5,
        "religion": "Muslim"
    }
}

print(person.keys())
print(person.values())

print(person)
person['name'] = 'Joseph'

print(person)
print(list(person))  # convert to list

print(person["other"])
print(person["other"]["marital_status"])
print(person["other"].get("height"))

# Update value
# person["other"].update({"religion":"Athesit"})
person["other"]["religion"] = 'Atheist'
print(person['other'])
print(person["other"].get("religion"))

# Add a key and value
person["socials"] = None
person["gender"] = "Male"
print(person)

# Loop through items
for items in person.values():
    print(items)

for items in person.keys():
    print(items)

# List items
print(person.items())
for key, value in person.items():
    print(f'for Key and value{key}, {value}')


# Remove items
# person['other'].pop("religion")
# print(person)

# # clear the dict
# person.clear()
# print(person)

# # delete the dict
# del person
# print(person)
