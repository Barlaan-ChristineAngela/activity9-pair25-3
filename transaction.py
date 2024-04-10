from customer import Customer

class Transaction:
    def __init__(self, customer, date):
        self.customer = customer
        self.date = date
        self.total = 0
        
    def calculate_transaction(self):
        transaction_total = 0
        
        for price in self.customer.wishlist:
            price = self.customer.wishlist[-1]
            
            transaction_total += price
            self.total = transaction_total
        
    def remove_books_from_wishlist(self):
        books_removed = 0
        
        for book in self.customer.wishlist:
            self.customer.wishlist.remove_book_from_wishlist(book)
            books_removed += 1
    
            
        
        

    

        
        
        
    
        
        