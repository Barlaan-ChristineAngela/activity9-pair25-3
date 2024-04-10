from wishlist import Wishlist

class Customer:
    def __init__(self, name, inventory):
        self.name = name
        self.wishlist = Wishlist(inventory)
        
    def add_book_to_wishlist(self, book):
        self.wishlist.add_book_to_wishlist(book)
        
    def view_wishlist(self):
        print(f"{self.name}'s Wishlist:")
        self.wishlist.view_wishlist()