# Class in python
class Person:
    def person1():
        return "Returning person 1"


print(Person.person1())


class House:
    def __init__(self, price, location, house_type):
        self.price = price
        self.location = location
        self.house_type = house_type

    def __str__(self) -> str:
        return f"We have a {self.house_type} house at {self.location} going for {self.price} US dollars."


house1 = House(3000, 'Texas', '3 Bedroom')
house2 = House(3500, 'Austin', '2 Bedroom')

# Modify values
house1.location = 'Minnesota'

print(house1)  # returns the string function
print(house1.price)
print(house1.location)

print(house2.price)
print(house2.location)


# Extend the parent class
class Client_details(House):
    def __init__(self, price, location, house_type, client_name):
        super().__init__(price, location, house_type)
        self.client_name = client_name

    def clients_info(self):
        return f"{self.client_name}  is our  recent client and has leased a {self.house_type} house in Austin.Hurry up and grab yours now!."


client_1 = Client_details(320, 'Westlands', '2 Bedroom', 'Becky')
print(client_1.clients_info())
