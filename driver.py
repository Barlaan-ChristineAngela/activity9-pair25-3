from book import Book
# from inventory import Inventory
from customer import Customer
from bookstore import bookStore
# Example Usage
if __name__ == "__main__":
    store = bookStore()
    store.add_customer("jon")
    store.add_book_to_inventory("lets go", 1)
    store.add_book_to_inventory("going off", 2)
    store.add_book_to_wishlist("going off", 1, "jon")
    store.remove_book_from_inventory("lets go")
    store.add_book_to_wishlist("lets go", 1, "jon")
    store.remove_book_from_wishlist("going off", 1, "jon")
    store.get_wishlist("jon")
