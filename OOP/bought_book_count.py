class Book:
    # Static Attribute(Only shared once)
    book_count = 0 

    def __init__(self,name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Book.book_count += 1
    
    def count_books_bought(self):
        print(f'{self.name}, {self.price}')
    
book1 = Book("Django book", 22.00, 33.0)
print(book1.book_count)
print(Book.book_count)
    
