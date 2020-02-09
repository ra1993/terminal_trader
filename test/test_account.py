import unittest
from app import Account

class TestAccount(unittest.TestCase):

    def test_account(self):
        
        user_1 = Account(None, None, "OreoAhoy", "1234", "Oreoo", "Ahoyyy", 900000, None)

        

if __name__ == "__main__":
    unittest.main()
