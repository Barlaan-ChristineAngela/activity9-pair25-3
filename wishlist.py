# from inventory import Inventory
class Wishlist:
    def __init__(self, inventory):
        self.wishlist = []
        self.available_books = inventory

    def add_book_to_wishlist(self, book):
        x = -1
        bookTitle = book.title
        for position, books in enumerate(self.available_books):
                if books.title == bookTitle:
                    x = position
        if x >= 0:
            self.wishlist.append(book)
            return True
        return False
    def check_inventory(self, book):
        if book in self.available_books:
            return True
        return False
    def remove_book_from_wishlist(self, book):
        x = -1
        bookTitle = book.title
        for position, books in enumerate(self.wishlist):
                if books.title == bookTitle:
                    x = position
        if x >= 0:
            self.wishlist.pop(x)
            return True
        return False

    def view_wishlist(self):
        if not self.wishlist:
            print("Wishlist is empty.")
        else:
            for book in self.wishlist:
                print(book.title)