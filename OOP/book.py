class Book:
    """ Book properties"""

    def __init__(self, name, description, price, is_available):
        self.name = name
        # self.__name = name,  Private attribute, Internal Use Only
        self.description = description
        self.price = price
        self.is_available = is_available


class Author(Book):
    def __init__(self, name, description, price, is_available, author):
        super().__init__(name, description, price, is_available)
        self.author = author

    def __str__(self):
        return f'Book Name: {self.name}, Author:{self.author}, Description: {self.description}, Price: {self.price}, Available: {self.is_available} '


book1 = Author("Django", "Django Fullstack Walkthrough", 30.00, True, "Alex")

print(book1)
