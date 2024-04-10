from customer import Customer
# from inventory import Inventory
from book import Book
from transaction import Transaction
class bookStore:
    def __init__(self):
        self.customer_list = []
        self.inventory = []
        self.transaction_list = []
        
    def add_customer(self, name):
        new_customer = Customer(name, self.inventory)
        self.customer_list.append(new_customer)
        
    def add_book_to_inventory(self, title, price):
        tempBook = Book(title, price)
        self.inventory.append(tempBook)
    
    def get_inventory(self):
        for book in self.inventory:
            print(book.title)
    
    def get_customer_list(self):
        print(self.customer_list[0].name)
    
    def get_wishlist(self, customer_name):
        x = -1
        for position, customer in enumerate(self.customer_list):
                if customer.name == customer_name:
                    x = position
        self.customer_list[x].wishlist.view_wishlist()

    def add_book_to_wishlist(self, title, price, customerName):
        x = -1
        for position, customer in enumerate(self.customer_list):
                if customer.name == customerName:
                    x = position
        if x >= 0:
            tempBook = Book(title, price)
            self.customer_list[x].add_book_to_wishlist(tempBook)
            return True
        else:
            return False
    
    def remove_book_from_inventory(self, book_title):
        x = -1
        for position, book in enumerate(self.inventory):
                if book.title == book_title:
                    x = position
        if x >= 0:
            self.inventory.pop(x)
    
    def remove_book_from_wishlist(self, title, price, customerName):
        x = -1
        for position, customer in enumerate(self.customer_list):
                if customer.name == customerName:
                    x = position
        if x >= 0:
            tempBook = Book(title, price)
            self.customer_list[x].wishlist.remove_book_from_wishlist(tempBook)
            return True
        else:
            return False
    
    def calculateTransaction(self, customerName):
        x = -1
        for position, customer in enumerate(self.customer_list):
                if customer.name == customerName:
                    x = position
        if x >= 0:
            tempTransaction = Transaction(self.customer_list[x], 0)
            self.transaction_list.append(tempTransaction)
            return True
        else:
            return False
    