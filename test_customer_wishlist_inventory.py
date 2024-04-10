import unittest
from customer import Customer
from book import Book
from bookstore import bookStore

class TestInventoryCustomerWishListRelationship(unittest.TestCase):
    
    #def test_add_book_to_customer_wishlist(self):
        #store = bookStore()
        
        #store.add_book_to_inventory("Jane Eyre", 18.99)
        
        #store.add_customer("Christine Barlaan")
        
        #result = store.add_book_to_wishlist("Jane Eyre", 18.99)
        
        #self.assertTrue(result)
        
        # result = customer.view_wishlist()
        
        # self.assertEqual(customer.wishlist.add_book_to_wishlist(newBook), print(result))
    
    #def test_add_invalid_book_to_customer_wishlist(self):
        #store = bookStore()
        
        #store.add_book_to_inventory("Jane Eyre", 18.99)
        #store.add_book_to_inventory("Dracula", 9.99)
        
        #store.add_customer("Christine Barlaan")
        
        #result = store.add_book_to_wishlist("hunger Games", 20.99)
        
        #self.assertFalse(result)
        
    def test_remove_book_to_customer_wishlist(self):
        store = bookStore()
        
        store.add_book_to_inventory("Jane Eyre", 18.99)
        store.add_book_to_inventory("Dracula", 9.99)
        
        
        store.add_customer("Christine Barlaan")

        store.add_book_to_wishlist("Jane Eyre", 18.99, "Christine Barlaan")
        result = store.remove_book_from_wishlist("Jane Eyre", 9.99, "Christine Barlaan")
        
        self.assertTrue(result)
        
if __name__ == "__main__":
    unittest.main()