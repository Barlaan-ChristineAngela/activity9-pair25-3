import unittest
from customer import Customer
from book import Book
from bookstore import bookStore

class TestTransactionWishlistRelationship(unittest.TestCase):
    
    def test_calculate_transaction(self):
        store = bookStore()
        
        store.add_book_to_inventory("Jane Eyre", 18.99)
        
        store.add_customer("Christine Barlaan")
        
        store.add_book_to_wishlist("Jane Eyre", 18.99, "christine")
        
        result = store.calculateTransaction("Christine Barlaan")
        
        self.assertTrue(result)
        